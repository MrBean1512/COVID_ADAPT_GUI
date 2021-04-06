import tkinter
import tkinter.font
from tkinter.constants import * # used for formatting
from tkinter.filedialog import askopenfile  # used to open a file
import os   # used for running an exe
import Window_Settings

def window_Prog():

    # define the main frame/window
    #window = tkinter.Frame(parent, relief=RIDGE, borderwidth=2)
    #window.pack(fill=BOTH, expand=1)

    tk = tkinter.Tk()
    tk.title("COVID ADAPT")

    # ==========================================================
    # define the right frame
    # this is where information is displayed
    rightFrame = tkinter.Frame(tk, relief = RIDGE, borderwidth = 2)
    rightFrame.pack(side = RIGHT)

    # define the Title label
    title = tkinter.Label(rightFrame, text = "Get Started")
    title.pack(fill = X, expand = 1)

    # ==========================================================
    # define the left frame
    # this is where the start page buttons should be held
    leftFrame = tkinter.Frame(tk, relief = RIDGE, borderwidth = 2)
    leftFrame.pack(side = LEFT)

    # button format
    buttonFont = tkinter.font.Font(family = "Helvetica", size = 16)
    buttonWidth = 20
    buttonJustify = "left"

    # define the new button
    def onClickNewSim():
        title.config(text = "Run Simulation")
        os.system('"C:/Windows/System32/notepad.exe"')
    buttonNewSim = tkinter.Button(leftFrame, text = "Run Simulation", font = buttonFont, width = buttonWidth, justify = buttonJustify, command = onClickNewSim)
    buttonNewSim.pack(side = TOP)

    # define the open button
    def onClickOpenSim():
        title.config(text = "Export")

    buttonOpenSim = tkinter.Button(leftFrame, text = "Export", font = buttonFont, width = buttonWidth, justify = buttonJustify, command = onClickOpenSim)
    buttonOpenSim.pack(side = TOP)

    # define the recent button
    def onClickRecentSim():
        title.config(text = "Settings")
        Window_Settings.window_Settings()
    buttonRecentSim = tkinter.Button(leftFrame, text = "Settings", font = buttonFont, width = buttonWidth, justify = buttonJustify, command = onClickRecentSim)
    buttonRecentSim.pack(side = TOP)

    # define the recent button
    def onClickRecentSim():
        title.config(text = "Edit Room")
    buttonRecentSim = tkinter.Button(leftFrame, text = "Edit Room", font = buttonFont, width = buttonWidth, justify = buttonJustify, command = onClickRecentSim)
    buttonRecentSim.pack(side = TOP)

    # define the exit button
    button = tkinter.Button(leftFrame, text = "Exit", font = buttonFont, width = buttonWidth, justify = buttonJustify, command = tk.destroy)
    button.pack(side = BOTTOM)

    # display the tkinter window
    tk.mainloop()