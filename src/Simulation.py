import tkinter
import tkinter.font
import Frame_Buttons
from tkinter.constants import * # used for formatting
from tkinter.filedialog import askopenfile  # used to open a file
import os   # used for running an exe
import Settings

def simulation(mainFrame, folderDirectory):

    # define the main frame/window
    #window = tkinter.Frame(parent, relief=RIDGE, borderwidth=2)
    #window.pack(fill=BOTH, expand=1)

    #tk = tkinter.Tk()
    #tk.title("COVID ADAPT")

    # ==========================================================
    # define the right frame
    # this is where information is displayed
    rightFrame = tkinter.Frame(mainFrame, relief = RIDGE, borderwidth = 2)
    rightFrame.pack(side = RIGHT)

    # define the Title label
    title = tkinter.Label(rightFrame, text = "Get Started")
    title.pack(fill = X, expand = 1)

    # ==========================================================
    # define the left frame
    # this is where the start page buttons should be held
    leftFrame = tkinter.Frame(mainFrame, relief = RIDGE, borderwidth = 2)
    leftFrame.pack(side = LEFT)

    # define the new button
    def run():
        title.config(text = "Run Simulation")
        os.system('"C:/Windows/System32/notepad.exe"')

    # define the open button
    def export():
        title.config(text = "Export")

    # define the recent button
    def settings():
        rightFrame.destroy()
        Settings.settings(mainFrame)

    # define the recent button
    def edit():
        title.config(text = "Edit Room")

    buttonSpecs = [
        #["name", function],
        ["Run Simulation", run],
        ["Export", export],
        ["Settings", settings],
        ["Edit Room", edit],
    ]

    Frame_Buttons.buttonBuilder(leftFrame, buttonSpecs)

    # display the tkinter window
    mainFrame.mainloop()