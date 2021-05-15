import tkinter
from tkinter.constants import *
import json
from tkinter.filedialog import askdirectory
import numpy as np
import pandas as pd
import Frame_Buttons

def Window_Space_Builder(mainFrame, folder):
    def readSettings():
        # read settings file into a map
        with open(folder + "/settings.json") as f:
            return json.load(f)


    leftFrame = tkinter.Frame(mainFrame)
    leftFrame.pack(side = LEFT)
    rightFrame = tkinter.Frame(mainFrame)
    rightFrame.pack(side = RIGHT)

    drawHeight = 600
    drawWidth = 600
    dotRadius = 1

    grid = tkinter.Canvas(leftFrame, height = drawHeight, width = drawWidth)
    grid.pack()

    settingsIn = readSettings()
    # the total number of possible walls on each axis
    gridsize_x = int(settingsIn["gridsize_x"])
    gridsize_y = int(settingsIn["gridsize_y"])
    wallsX = gridsize_x + 1
    wallsY = gridsize_y + 1
    wallsXLength = float(drawWidth - dotRadius * 4) / gridsize_x
    wallsYLength = float(drawHeight - dotRadius * 4) / gridsize_y

    #csv format
    #EWNS all columns in row 1 then row 2, etc.
    layout = pd.DataFrame(np.zeros((gridsize_x * gridsize_y , 4))) # to be turned into layout.csv; contains walls at the 4 edges of every grid space
    layout = layout + 1
    layout["room"] = "outside"

    # displays a dot at every grid location
    def drawDots():
        i = 0
        j = 0
        while i < gridsize_x + 2:
            while j < gridsize_y + 2:
                centerX = i * wallsXLength + dotRadius * 4
                centerY = j * wallsYLength + dotRadius * 4
                x1 = centerX + dotRadius
                y1 = centerY + dotRadius
                x2 = centerX - dotRadius
                y2 = centerY - dotRadius
                grid.create_oval(x1, y1, x2, y2)
                j += 1
            i += 1
            j = 0

    # Store the position of two clicks then draw a line between the two positions.
    def getClick(eventOrigin):
        global posX1, posY1, posX2, posY2, x1, y1

        firstClick = FALSE
        try:
            posX1
        except NameError:
            firstClick = TRUE # if x1 has never been set, this is the very first click

        if firstClick == FALSE and posX1 == -1:
            firstClick = TRUE # if x1 is set to -1 the second click happened last time

        if firstClick:
            x1 = eventOrigin.x - (dotRadius * 4) #adjust for the offset of the dots/grid
            y1 = eventOrigin.y - (dotRadius * 4)
            posX1 = round(round(x1 / wallsXLength) * wallsXLength)
            posY1 = round(round(y1 / wallsYLength) * wallsYLength)
        else:
            x2 = eventOrigin.x - (dotRadius * 4)
            y2 = eventOrigin.y - (dotRadius * 4)
            posX2 = round(round(x2 / wallsXLength) * wallsXLength)
            posY2 = round(round(y2 / wallsYLength) * wallsYLength)
            #choose to draw a horizontal or vertical line based on which dimension has a greater difference


    #csv format
    #EWNS all columns in row 1 then row 2, etc.
            if abs(posX2 - posX1) > abs(posY2 - posY1):
                posY2 = posY1
                wallX1 = round(x1 / wallsXLength) # the position of the wall in terms of the grid
                wallX2 = round(x2 / wallsXLength)
                wallY = round(y1/wallsYLength)

                if wallX2 < wallX1:
                    temp = wallX2
                    wallX2 = wallX1
                    wallX1 = temp
                #run along the x-axis where the wall is to populate the csv
                for i in range((wallY * gridsize_x) + wallX1, (wallY * gridsize_x) + wallX2):
                    #block lower space's north wall if the wall is not the last row
                    if wallY < gridsize_y: 
                        layout.at[i,2] = 0
                    # block upper space's south wall if the wall is not on the first row
                    if wallY > 0:
                        layout.at[i - gridsize_x, 3] = 0
            else:
                posX2 = posX1
                wallY1 = round(y1/wallsYLength)
                wallY2 = round(y2/wallsYLength)
                wallX = round(x1/wallsXLength)

                if wallY2 < wallY1:
                    temp = wallY2
                    wallY2 = wallY1
                    wallY1 = temp
                #run along the y-axis where the wall is to populate the csv
                i = (wallY1 * gridsize_x) + wallX
                while i < (wallY2 * gridsize_x) + wallX:
                    #block left space's east wall if the wall is not the first column
                    if wallX > 0:
                        layout.at[i-1, 0] = 0
                    # block right space's west wall if the wall is not on the last column
                    if wallX < gridsize_x:
                        layout.at[i, 1] = 0
                    i += gridsize_x

            grid.create_line(posX1 + dotRadius * 4, posY1 + dotRadius * 4, posX2 + dotRadius * 4, posY2 + dotRadius * 4, fill = "red")
            #print("x2:" + str(x2) + " y2:" + str(y2))
            #print("posX1:" + str(posX1) + " posY1:" + str(posY1) + " posX2:" + str(posX2) + " posY2:" + str(posY2))
            posX1 = -1

    def saveSpace():
        layout.to_csv(folder + "/layout.csv", header = FALSE, index = FALSE)
        leftFrame.destroy()
        rightFrame.destroy()

    def cancel():
        leftFrame.destroy()
        rightFrame.destroy()

    buttonSpecs = [
        #["name", function],
        ["Cancel", cancel],
        ["Save", saveSpace]
    ]

    Frame_Buttons.buttonBuilder(rightFrame, buttonSpecs)

    grid.bind("<Button 1>", getClick)

    drawDots()