import tkinter
import tkinter.font
from tkinter.constants import *


# TODO
# make sure that the button builder builds a whole frame
# make sure that all other files that use this have updated changes
def buttonBuilder(parentFrame, buttonSpecs):
    # button format
    buttonFont = tkinter.font.Font(family = "Helvetica", size = 16)
    buttonWidth = 20
    buttonJustify = tkinter.LEFT

    parentFrame.button = []

    for i in range(0, len(buttonSpecs)):
        parentFrame.button.append(tkinter.Button(parentFrame, 
        text = buttonSpecs[i][0], 
        font = buttonFont, 
        width = buttonWidth, 
        justify = buttonJustify, 
        command = buttonSpecs[i][1]))

        parentFrame.button[i].pack(side = TOP)