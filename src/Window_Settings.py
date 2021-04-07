# settings window which is accessed through the main window under open sim
import tkinter
import tkinter.font
from tkinter.constants import *
from tkinter.filedialog import askopenfile
import json

# subclass of Entry that holds the name of the variable in the settings file that the entry corresponds with
class settingEntry(tkinter.Entry):
    def __init__(self, master, *args, **kwargs):
        tkinter.Entry.__init__(self, master, *args, **kwargs)
        self.variableName = "unnamed"
        self.default = ""

def window_Settings():
    tk = tkinter.Tk()
    tk.title("COVID ADAPT")

    # top frame holds left and right frames
    topFrame = tkinter.Frame(tk)
    topFrame.pack(side = TOP)

    # left frame holds setting names
    leftFrame = tkinter.Frame(topFrame)
    leftFrame.pack(side = LEFT)

    # right frame holds setting entry boxes
    rightFrame = tkinter.Frame(topFrame)
    rightFrame.pack(side = RIGHT)

    # bottom frame holds buttons
    bottomFrame = tkinter.Frame(tk)
    bottomFrame.pack(side = BOTTOM)

    # define steepness exposure entry
    labelSteepnessExposure = tkinter.Label(leftFrame, text = "Steepness Exposure")
    labelSteepnessExposure.pack(side = TOP)
    entrySteepnessExposure = settingEntry(rightFrame)
    entrySteepnessExposure.variableName = "steepness_exposure"
    entrySteepnessExposure.default = 1
    entrySteepnessExposure.pack(side = TOP)
    
    #define steepness infectious entry
    labelSteepnessInfectious = tkinter.Label(leftFrame, text = "Steepness Infection")
    labelSteepnessInfectious.pack(side = TOP)
    entrySteepnessInfectious = settingEntry(rightFrame)
    entrySteepnessInfectious.variableName = "steepness_infectious"
    entrySteepnessInfectious.default = 1
    entrySteepnessInfectious.pack(side = TOP)

    # define midpoint infectious entry
    labelMidpointInfectious = tkinter.Label(leftFrame, text = "Midpoint Infectious")
    labelMidpointInfectious.pack(side = TOP)
    entryMidpointInfectious = settingEntry(rightFrame)
    entryMidpointInfectious.variableName = "midpoint_infectious"
    entryMidpointInfectious.default = 7200
    entryMidpointInfectious.pack(side = TOP)

    # define steepness recovery
    labelSteepnessRecovery = tkinter.Label(leftFrame, text = "Steepness Recovery")
    labelSteepnessRecovery.pack(side = TOP)
    entrySteepnessRecovery = settingEntry(rightFrame)
    entrySteepnessRecovery.variableName = "steepness_recovery"
    entrySteepnessRecovery.default = 1
    entrySteepnessRecovery.pack(side = TOP)

    # define midpoint recovery
    labelMidpointRecovery = tkinter.Label(leftFrame, text = "Midpoint Recovery")
    labelMidpointRecovery.pack(side = TOP)
    entryMidpointRecovery = settingEntry(rightFrame)
    entryMidpointRecovery.variableName = "midpoint_recovery"
    entryMidpointRecovery.default = 14400
    entryMidpointRecovery.pack(side = TOP)

    # define virus decay rate
    labelVirusDecayRate = tkinter.Label(leftFrame, text = "Virus Decay Rate")
    labelVirusDecayRate.pack(side = TOP)
    entryVirusDecayRate = settingEntry(rightFrame)
    entryVirusDecayRate.variableName = "virus_decay_rate"
    entryVirusDecayRate.default = 0.001
    entryVirusDecayRate.pack(side = TOP)

    # define number infectious
    labelNumberInfectious = tkinter.Label(leftFrame, text = "Number Infectious")
    labelNumberInfectious.pack(side = TOP)
    entryNumberInfectious = settingEntry(rightFrame)
    entryNumberInfectious.variableName = "number_infectious"
    entryNumberInfectious.default = 4
    entryNumberInfectious.pack(side = TOP)

    # define number susceptible
    labelNumberSusceptible = tkinter.Label(leftFrame, text = "Number Susceptible")
    labelNumberSusceptible.pack(side = TOP)
    entryNumberSusceptible = settingEntry(rightFrame)
    entryNumberSusceptible.variableName = "number_susceptible"
    entryNumberSusceptible.default = 6
    entryNumberSusceptible.pack(side = TOP)

    # define gridsize x
    labelGridsizeX = tkinter.Label(leftFrame, text = "Gridsize X")
    labelGridsizeX.pack(side = TOP)
    entryGridsizeX = settingEntry(rightFrame)
    entryGridsizeX.variableName = "gridsize_x"
    entryGridsizeX.default = 43
    entryGridsizeX.pack(side = TOP)

    # define gridsize y
    labelGridsizeY = tkinter.Label(leftFrame, text = "Gridsize Y")
    labelGridsizeY.pack(side = TOP)
    entryGridsizeY = settingEntry(rightFrame)
    entryGridsizeY.variableName = "gridsize_y"
    entryGridsizeY.default = 43
    entryGridsizeY.pack(side = TOP)

    # define max time
    labelMaxTime = tkinter.Label(leftFrame, text = "Max Time")
    labelMaxTime.pack(side = TOP)
    entryMaxTime = settingEntry(rightFrame)
    entryMaxTime.variableName = "max_time"
    entryMaxTime.default = 30000
    entryMaxTime.pack(side = TOP)

    # define midpoint exposure
    labelMidpointExposure = tkinter.Label(leftFrame, text = "Midpoint Exposure")
    labelMidpointExposure.pack(side = TOP)
    entryMidpointExposure = settingEntry(rightFrame)
    entryMidpointExposure.variableName = "midpoint_exposure"
    entryMidpointExposure.default = 50
    entryMidpointExposure.pack(side = TOP)

    # store all entry objects in a list
    entries = [widget for widget in rightFrame.winfo_children() if isinstance(widget, settingEntry)]

    # define back  button
    # closes the settings window and returns to the main window
    backButton = tkinter.Button(bottomFrame, text = "Return To Menu", command = tk.destroy)
    backButton.pack(side = BOTTOM)

    # define save button
    # the save button creates a map containing every setting and value and outputs the map to a JSON file
    settings = {}
    def saveSettings():
        for entry in entries:
            settings[entry.variableName] = entry.get() 

        outFile = open("settings.json", "w")
        outFile.write(json.dumps(settings))
        outFile.close()

    saveButton = tkinter.Button(bottomFrame, text = "Save Settings", command = saveSettings)
    saveButton.pack(side = BOTTOM)

    # define defaults button
    # default button sets all entries to default values and saves these new values to the settings file
    def setAsDefaults():
        for entry in entries:
            entry.delete(0, END)
            entry.insert(0, entry.default)
        saveSettings()

    defaultButton = tkinter.Button(bottomFrame, text = "Set Default Values", command = setAsDefaults)
    defaultButton.pack(side = BOTTOM)

    # display the window
    tk.mainloop()