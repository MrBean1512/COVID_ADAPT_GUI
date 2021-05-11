import tkinter
import tkinter.font
import Welcome
import Frame_Buttons
import ExportVideo
from tkinter.constants import * # used for formatting
from tkinter.filedialog import askopenfile  # used to open a file
import os   # used for running an exe
import Settings
from threading import Thread
# import subprocess

def simulation(window, mainFrame, folderDirectory):

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
#        title.config(text = "Run Simulation")
        os.chdir(folderDirectory)
        print("working directory updated\nrunning simulation...")
        os.system(folderDirectory + '/COVID-ADAPT.exe')
        print("Done Running")
        # subprocess.run(folderDirectory + '/COVID-ADAPT.exe', capture_output=True)

    def threadRun():
        t1 = Thread(target = run)
        t1.start()

    # define the open button
    def export():
        title.config(text = "Export")
        ExportVideo.videoGen(folderDirectory)

    # define the recent button
    def settings():
        rightFrame.destroy()
        Settings.settings(mainFrame, folderDirectory)

    # define the recent button
    def exit():
        leftFrame.destroy()
        rightFrame.destroy()
        Welcome.welcome(window, mainFrame)

    buttonSpecs = [
        #["name", function],
        ["Run Simulation", run], #TODO change function to threadRun once multithreading is fully functional
        ["Export", export],
        ["Settings", settings],
        ["Return to Menu", exit],
    ]

    Frame_Buttons.buttonBuilder(leftFrame, buttonSpecs)

    # display the tkinter window
    mainFrame.mainloop()