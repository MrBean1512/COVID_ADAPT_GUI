import tkinter
import tkinter.font
from tkinter.constants import *
from tkinter.filedialog import askopenfile

def window_Settings():
    tk = tkinter.Tk()
    tk.title("COVID ADAPT")

    # left frame holds setting names
    leftFrame = tkinter.Frame(tk)
    leftFrame.pack(side = LEFT)

    # right frame holds setting entry boxes
    rightFrame = tkinter.Frame(tk)
    rightFrame.pack(side = RIGHT)

    # define steepness exposure entry
    labelSteepnessExposure = tkinter.Label(leftFrame, text = "Steepness Exposure")
    labelSteepnessExposure.pack(side = TOP)
    entrySteepnessExposure = tkinter.Entry(rightFrame)
    entrySteepnessExposure.pack(side = TOP)
    
    #define steepness infection entry
    labelSteepnessInfection = tkinter.Label(leftFrame, text = "Steepness Infection")
    labelSteepnessInfection.pack(side = TOP)
    entrySteepnessInfection = tkinter.Entry(rightFrame)
    entrySteepnessInfection.pack(side = TOP)

    # define midpoint infectious entry
    labelMidpointInfectious = tkinter.Label(leftFrame, text = "Midpoint Infectious")
    labelMidpointInfectious.pack(side = TOP)
    entryMidpointInfectious = tkinter.Entry(rightFrame)
    entryMidpointInfectious.pack(side = TOP)

    # define submit button
    # saves changes to settings file

    # define back  button
    # returns to the main window

    # display the window
    tk.mainloop()