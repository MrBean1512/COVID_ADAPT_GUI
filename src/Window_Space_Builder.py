import tkinter
from tkinter.constants import *
import json

def Window_Space_Builder():
    def readSettings():
        # read settings file into a map
        with open("./settings.json") as f:
            return json.load(f)

    tk = tkinter.Tk()
    tk.title("COVID ADAPT")

    leftFrame = tkinter.Frame(tk)
    leftFrame.pack(side = LEFT)

    drawHeight = 700
    drawWidth = 700
    dotRadius = 1
    rightFrame = tkinter.Frame(tk)
    rightFrame.pack(side = RIGHT)

    grid = tkinter.Canvas(rightFrame, height = drawHeight, width = drawWidth)
    grid.pack()


    labelOne = tkinter.Label(leftFrame, text = "Click once to choose the starting location of a wall.\n Click again to choose the end location.")
    labelOne.pack(side = TOP)

    settingsIn = readSettings()
    # the total number of possible walls on each axis
    gridsize_x = int(settingsIn["gridsize_x"])
    gridsize_y = int(settingsIn["gridsize_y"])
    wallsX = gridsize_x + 1
    wallsY = gridsize_y + 1
    wallsXLength = float(drawWidth) / gridsize_x
    wallsYLength = float(drawHeight) / gridsize_y

    # displays a dot at every grid location
    def drawDots():
        i = 0
        j = 0
        while i < gridsize_x:
            while j < gridsize_y:
                centerX = i * wallsXLength
                centerY = j * wallsYLength
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
        global posX1, posY1, posX2, posY2

        firstClick = FALSE
        try:
            posX1
        except NameError:
            firstClick = TRUE # if x1 has never been set, this is the very first click

        if firstClick == FALSE and posX1 == -1:
            firstClick = TRUE # if x1 is set to -1 the second click happened last time

        if firstClick:
            x1 = eventOrigin.x
            y1 = eventOrigin.y
            posX1 = round(round(x1 / wallsXLength) * wallsXLength)
            posY1 = round(round(y1 / wallsYLength) * wallsYLength)
            #print("x1:" + str(x1) + " y1:" + str(y1))

        else:
            x2 = eventOrigin.x
            y2 = eventOrigin.y
            posX2 = round(round(x2 / wallsXLength) * wallsXLength)
            posY2 = round(round(y2 / wallsYLength) * wallsYLength)
            #choose to draw a horizontal or vertical line based on which dimension has a greater difference
            if abs(posX2 - posX1) > abs(posY2 - posY1):
                posY2 = posY1
            else:
                posX2 = posX1
            grid.create_line(posX1, posY1, posX2, posY2, fill = "red")
            #print("x2:" + str(x2) + " y2:" + str(y2))
            #print("posX1:" + str(posX1) + " posY1:" + str(posY1) + " posX2:" + str(posX2) + " posY2:" + str(posY2))
            posX1 = -1


    grid.bind("<Button 1>", getClick)

    drawDots()

    tk.mainloop()

    #csv format
    #EWNS all columns in row 1 then row 2, etc.