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
    print("begining video export")
    dir = dir + '\\'
    if not os.path.isfile(dir+'virus_levels.csv'):
        print("unable to open virus_levels.csv")
        return False
    if not os.path.isfile(dir+'layout.csv'):
        print("unable to open layout.csv")
        return False
    if not os.path.isfile(dir+'people.csv'):
        print("unable to open people.csv")
        return False

    startTime = time.time()

    virusLevels = pd.read_csv(dir+'virus_levels.csv')
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
    video = VideoWriter(dir+"output.mp4", fourcc, float(FPS), (width, height))

    tileSize = int(2**(np.floor(np.log2(height/dim))-1)) # size of block in pixels, round to nearest power of 2 (8, 16, 32..etc)

    layout = np.full((height, width, 3), 255, dtype = np.uint8) #initialize to white
    # draw walls from layout.csv
    layoutData = pd.read_csv(dir+'layout.csv', header=None, names=['e', 'w', 'n', 's', 'tag'])

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

    # title text properties
    text_center = (int(width/2), int(height/8))
    text_font = cv2.FONT_HERSHEY_SIMPLEX
    text_scale = 1
    text_color = (0,0,0)
    text_thickness = 1
    text_str = "Timepoint (minutes): " + str( virusLevels.iloc[totalTimes-1, 0] ) # reference last time to determine title location
    text_width, text_height = cv2.getTextSize(text_str, text_font, text_scale, text_thickness)[0]
    text_origin = (int( text_center[0] - (text_width/2) ), int( text_center[1] - (text_height/2) ) )

    # text_str = "Title"
    # text_width, text_height = cv2.getTextSize(text_str, text_font, text_scale, text_thickness)[0]
    # text_origin = (int( text_center[0] - (text_width/2) ), int( text_center[1] - (text_height/2) ) )
    # background = cv2.putText(layout, text_str, text_origin, text_font, text_scale, text_color, text_thickness, cv2.LINE_AA)
    background = np.copy(layout)

    # draw legend
    legend_x_0 = int(0.8*width)
    legend_x_1 = int(0.81*width)
    legend_y_0 = int(0.35*height)
    legend_y_1 = int(0.65*height)
    # legend outline
    for x in range(legend_x_0,legend_x_1):
        background[legend_y_0][x] = [0, 0, 0]
        background[legend_y_1+1][x] = [0, 0, 0]

    for y in range(legend_y_0,legend_y_1+2):
        background[y][legend_x_0] = [0, 0, 0]
        background[y][legend_x_1] = [0, 0, 0]
    incrimentSize = (legend_y_1-legend_y_0)/10
    for i in range (0,10):
        # write legend text
        text_str = str(int((i+1) * max_virus_level/10))
        background = cv2.putText(background, text_str, (legend_x_1 + int(0.015*width), legend_y_1 - int((i+0.75) * incrimentSize)), text_font, text_scale/2, text_color, text_thickness, cv2.LINE_AA)
        for x in range(1, int(0.01*width)):
            # legend tick marks
            background[legend_y_0 + int(i * incrimentSize)][legend_x_1 + x] = [0, 0, 0]
            # legend color fill
            for y in range(int(i * incrimentSize)+1, int((i+1) * incrimentSize)+1):
                background[legend_y_0 + y][legend_x_0 + x] = [(i*25), (i*25), 255]

    # cv2.imwrite('background.jpg', background)

    people = pd.read_csv(dir+'people.csv')
    num_people = 10 # fix magic number from settings
    # totalTimes = int(np.sqrt(totalTimes))
    for timeStep in progressbar(range( totalTimes ), "Computing: ", 40):
        img = np.copy(background)
        # add title
        text_str = "Timepoint (minutes): " + str( virusLevels.iloc[timeStep, 0] )
        img = cv2.putText(img, text_str, text_origin, text_font, text_scale, text_color, text_thickness, cv2.LINE_AA)
        # fill in virus levels
        for tileIndex in range(0, totalTiles):
            if virusLevels.iloc[timeStep, tileIndex + 1] > threshold:
                r = tileIndex // dim
                c = tileIndex % dim
                y = layout_y_0 + (r * tileSize)
                x = layout_x_0 + (c * tileSize)
                redOffset = 255 - min(int(255 * virusLevels.iloc[timeStep, tileIndex + 1] / max_virus_level), 255)
                for i in range(1, tileSize):
                    for j in range(1, tileSize):
                        img[y+i][x+j] = [redOffset, redOffset, 255]
        # draw people
        for n in range(0, num_people):
            pos = people[' position'][n + (timeStep*num_people)]
            r = pos // dim
            c = pos % dim
            y = layout_y_0 + (r * tileSize)
            x = layout_x_0 + (c * tileSize)
            for i in range(int(tileSize * (0.25))+1, int(tileSize * (.75))):
                for j in range(int(tileSize * (0.25)+1), int(tileSize * (.75))):
                    img[y+i][x+j] = [0, 0, 0]

        # cv2.imwrite('frame'+str(timeStep)+'.jpg', img)
        video.write(img)

    video.release()
    endTime = time.time()

    elapsedTime = str( datetime.timedelta(seconds=np.floor(endTime - startTime)) )
    print("export completed in ", elapsedTime)