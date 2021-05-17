import Welcome
import Frame_Buttons
import ExportVideo
import Window_Space_Builder
import Graphs

import tkinter
import tkinter.font
from tkinter.constants import * # used for formatting
from tkinter.filedialog import askopenfile  # used to open a file

import os   # used for running an exe
import Settings
from threading import Thread

#from Window_Space_Builder import Window_Space_Builder
# import subprocess

def simulation(window, mainFrame, folderDirectory):

    # ==========================================================
    # define the right frame
    # this is where information is displayed
    rightFrame = tkinter.Frame(mainFrame, relief = RIDGE, borderwidth = 2)
    rightFrame.pack(side = RIGHT)

    # define the Title label
    Graphs.graphFrame(rightFrame, folderDirectory)

    # ==========================================================
    # define the left frame
    # this is where the start page buttons should be held
    leftFrame = tkinter.Frame(mainFrame, relief = RIDGE, borderwidth = 2)
    leftFrame.pack(side = LEFT)

    # define the new button
    def run():
        #title.config(text = "Run Simulation")
        mainWDir = os.getcwd()
        os.chdir(folderDirectory)
        print("working directory updated\nrunning simulation...")
        os.system(folderDirectory + '/COVID-ADAPT.exe')
        os.chdir(mainWDir)
        print("Done Running. \nGenerating images...")
        Graphs.makeGraphs()
        # destroy all widgets from frame
        for widget in rightFrame.winfo_children():
            widget.destroy()
        Graphs.graphFrame(rightFrame, folderDirectory)
        print("Done generating graphs.")
        # subprocess.run(folderDirectory + '/COVID-ADAPT.exe', capture_output=True)

    # use this to run the simulation on another thread
    # WARNING: this is not used because it creates a few dangerous issues
    def threadRun():
        t1 = Thread(target = run)
        t1.start()

    # define the open button
    def export():
        ExportVideo.videoGen(folderDirectory)

    # define the recent button
    def settings():
        for widget in rightFrame.winfo_children():
            widget.destroy()
        Settings.settings(rightFrame, folderDirectory)

    # define the recent button
    def exit():
        leftFrame.destroy()
        rightFrame.destroy()
        Welcome.welcome(window, mainFrame)

    def edit():
        Window_Space_Builder.Window_Space_Builder(mainFrame, folderDirectory)

    buttonSpecs = [
        #["name", function],
        ["Run Simulation", run], #TODO change function to threadRun once multithreading is fully functional
        ["Export", export],
        ["Settings", settings],
        ["Return to Menu", exit],
        ["Edit Space (Experimental)", edit]
    ]

    Frame_Buttons.buttonBuilder(leftFrame, buttonSpecs)

    # display the tkinter window
    mainFrame.mainloop()