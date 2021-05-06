import pandas as pd
import os
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
import numpy as np
import sys
import time
import datetime

def progressbar(it, prefix="", size=60, file=sys.stdout):
    startTime = time.time()
    count = len(it)
    def show(j):
        x = int(size*j/count)
        elapsedTime = time.time() - startTime
        timeToComplete = elapsedTime * (count / (j))
        finishedIn = startTime + timeToComplete - time.time()
        timeRemaining = str( datetime.timedelta(seconds=np.floor(finishedIn)) )
        file.write("%s[%s%s] %i/%i time remaining %s\r" % (prefix, "#"*x, "."*(size-x), j, count, timeRemaining))
        file.flush()        
    # show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


def videoGen(dir):
    if not os.path.isfile(dir+'\\virus_levels.csv'):
        print("virus_levels.csv not found. Try running the simulation to generate it.")
        return False
    if not os.path.isfile(dir+'\\layout.csv'):
        print("layout.csv not found. Try running the simulation to generate it.")
        return False
    if not os.path.isfile(dir+'\\people.csv'):
        print("people.csv not found. Try running the simulation to generate it.")
        return False

    virusLevels = pd.read_csv(dir+'/virus_levels.csv')
    # delete empty column????
    virusLevels = virusLevels.drop(virusLevels.columns[[1]], axis = 1)
    # remove once this column is gone in cpp code!!!

    # get parameters 
    # TODO get these from settings files
    totalTimes = virusLevels.shape[0] # number of time entries
    totalTiles = virusLevels.shape[1] - 1 # number of boxes
    dim = int(np.sqrt(totalTiles)) # assumes square simulation

    # video properties
    width = 1280
    height = 720
    FPS = 60
    # init video
    fourcc = VideoWriter_fourcc(*'mp4v')
    video = VideoWriter(dir + '/output.mp4', fourcc, float(FPS), (width, height))

    tileSize = int(2**(np.floor(np.log2(height/dim))-1)) # size of block in pixels, round to nearest power of 2 (8, 16, 32..etc)

    layout = np.full((height, width, 3), 255, dtype = np.uint8) #initialize to white
    # draw walls from layout.csv
    layoutData = pd.read_csv(dir+'/layout.csv', header=None, names=['e', 'w', 'n', 's', 'tag'])

    layout_x_0 = int( (width - (tileSize*dim))/2 )
    layout_y_0 = int( (height - (tileSize*dim))/2)

    for index, row in layoutData.iterrows():
        # print(index, row['n'], row['s'], row['e'], row['w'])
        r = index // dim # row index
        c = index % dim # column index
        # pixel location of tile origin
        y = layout_y_0 + (r * tileSize)
        x = layout_x_0 + (c * tileSize)

        color = row['n'] * 200 # choose color based on if the direction is closed or not (0 (black) for closed, 200 (grey) for open)
        for i in range(0, tileSize): #assign the next 16 pixels in a line to this color
            layout[y][x + i] = [color,color,color]
        # repeat for each other direction
        color = row['s'] * 200
        for i in range(0, tileSize):
            layout[y + tileSize][x + i] = [color,color,color]
        color = row['e'] * 200
        for i in range(0, tileSize):
            layout[y + i][x] = [color,color,color]
        color = row['w'] * 200
        for i in range(0, tileSize):
            layout[y + i][x + tileSize] = [color,color,color]

    # find max of each row (excluding timesetp column), find max of said list
    max_virus_level = virusLevels.iloc[:,1:].max().max()
    threshold = (1/255)*max_virus_level # used to limit minumum value that prgram will color in cells
    # cv2.imwrite('layout.jpg', layout)

    for timeStep in progressbar(range(totalTimes), "Computing: ", 40):
        # print("Time: ", virusLevels.iloc[timeStep, 0])
        for tileIndex in range(0, totalTiles):
            img = layout
            if virusLevels.iloc[timeStep, tileIndex + 1] > threshold:
                r = tileIndex // dim
                c = tileIndex % dim
                y = layout_y_0 + (r * tileSize)
                x = layout_x_0 + (c * tileSize)
                redOffset = 255 - min(int(255 * virusLevels.iloc[timeStep, tileIndex + 1] / max_virus_level), 255)
                for i in range(1, tileSize):
                    for j in range(1, tileSize):
                        img[y+i][x+j] = [redOffset, redOffset, 255]
        # cv2.imwrite('frame'+str(timeStep)+'.jpg', img)
        video.write(img)

    video.release()

#fpath = '..\COVID-ADAPT_archive\\'

#videoGen(fpath)