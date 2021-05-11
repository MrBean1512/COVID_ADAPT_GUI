# settings window which is accessed through the main window under open sim
import tkinter
import tkinter.font
from tkinter.constants import *
from tkinter.filedialog import askopenfile
import json
import Frame_Buttons
import Graphs

# subclass of Entry that holds the name of the variable in the settings file that the entry corresponds with
class settingEntry(tkinter.Entry):
    def __init__(self, master, *args, **kwargs):
        tkinter.Entry.__init__(self, master, *args, **kwargs)
        self.variableName = "unnamed"
        self.default = ""
        self.type = int

def settings(mainFrame, folderDirectory):
    settingsFrame = tkinter.Frame(mainFrame)
    settingsFrame.pack(side = RIGHT)

    # top frame holds left and right frames
    topFrame = tkinter.Frame(settingsFrame)
    topFrame.pack(side = TOP)

    # left frame holds setting names
    leftFrame = tkinter.Frame(topFrame)
    leftFrame.pack(side = LEFT)

    # right frame holds setting entry boxes
    rightFrame = tkinter.Frame(topFrame)
    rightFrame.pack(side = RIGHT)

    # bottom frame holds buttons
    bottomFrame = tkinter.Frame(settingsFrame)
    bottomFrame.pack(side = BOTTOM)

    # define steepness exposure entry
    labelSteepnessExposure = tkinter.Label(leftFrame, text = "Steepness Exposure")
    labelSteepnessExposure.pack(side = TOP)
    entrySteepnessExposure = settingEntry(rightFrame)
    entrySteepnessExposure.variableName = "steepness_exposure"
    entrySteepnessExposure.default = 1
    entrySteepnessExposure.type = "decimal"
    entrySteepnessExposure.pack(side = TOP)
    
    #define steepness infectious entry
    labelSteepnessInfectious = tkinter.Label(leftFrame, text = "Steepness Infection")
    labelSteepnessInfectious.pack(side = TOP)
    entrySteepnessInfectious = settingEntry(rightFrame)
    entrySteepnessInfectious.variableName = "steepness_infectious"
    entrySteepnessInfectious.default = 1
    entrySteepnessInfectious.type = "decimal"
    entrySteepnessInfectious.pack(side = TOP)

    # define midpoint infectious entry
    labelMidpointInfectious = tkinter.Label(leftFrame, text = "Midpoint Infectious")
    labelMidpointInfectious.pack(side = TOP)
    entryMidpointInfectious = settingEntry(rightFrame)
    entryMidpointInfectious.variableName = "midpoint_infectious"
    entryMidpointInfectious.default = 7200
    entryMidpointInfectious.type = "decimal"
    entryMidpointInfectious.pack(side = TOP)

    # define steepness recovery
    labelSteepnessRecovery = tkinter.Label(leftFrame, text = "Steepness Recovery")
    labelSteepnessRecovery.pack(side = TOP)
    entrySteepnessRecovery = settingEntry(rightFrame)
    entrySteepnessRecovery.variableName = "steepness_recovery"
    entrySteepnessRecovery.default = 1
    entrySteepnessRecovery.type = "decimal"
    entrySteepnessRecovery.pack(side = TOP)

    # define midpoint recovery
    labelMidpointRecovery = tkinter.Label(leftFrame, text = "Midpoint Recovery")
    labelMidpointRecovery.pack(side = TOP)
    entryMidpointRecovery = settingEntry(rightFrame)
    entryMidpointRecovery.variableName = "midpoint_recovery"
    entryMidpointRecovery.default = 14400
    entryMidpointRecovery.type = "decimal"
    entryMidpointRecovery.pack(side = TOP)

    # define virus decay rate
    labelVirusDecayRate = tkinter.Label(leftFrame, text = "Virus Decay Rate")
    labelVirusDecayRate.pack(side = TOP)
    entryVirusDecayRate = settingEntry(rightFrame)
    entryVirusDecayRate.variableName = "virus_decay_rate"
    entryVirusDecayRate.default = 0.001
    entryVirusDecayRate.type = "decimal"
    entryVirusDecayRate.pack(side = TOP)

    # define vaccine efficacy
    labelVirusDecayRate = tkinter.Label(leftFrame, text = "Vaccine efficacy")
    labelVirusDecayRate.pack(side = TOP)
    entryVirusDecayRate = settingEntry(rightFrame)
    entryVirusDecayRate.variableName = "vaccine_efficacy"
    entryVirusDecayRate.default = 0.75
    entryVirusDecayRate.type = "decimal"
    entryVirusDecayRate.pack(side = TOP)

    # define number infectious
    labelNumberInfectious = tkinter.Label(leftFrame, text = "Number Infectious")
    labelNumberInfectious.pack(side = TOP)
    entryNumberInfectious = settingEntry(rightFrame)
    entryNumberInfectious.variableName = "number_infectious"
    entryNumberInfectious.default = 4
    entryNumberInfectious.type = "int"
    entryNumberInfectious.pack(side = TOP)

    # define number susceptible vaccinated
    labelNumberSusceptible = tkinter.Label(leftFrame, text = "Number Susceptible Vaccinated")
    labelNumberSusceptible.pack(side = TOP)
    entryNumberSusceptible = settingEntry(rightFrame)
    entryNumberSusceptible.variableName = "number_susceptible_vaccinated"
    entryNumberSusceptible.default = 6
    entryNumberSusceptible.type = "int"
    entryNumberSusceptible.pack(side = TOP)

    # define number susceptible unvaccinated
    labelNumberSusceptible = tkinter.Label(leftFrame, text = "Number Susceptible Unvaccinated")
    labelNumberSusceptible.pack(side = TOP)
    entryNumberSusceptible = settingEntry(rightFrame)
    entryNumberSusceptible.variableName = "number_susceptible_unvaccinated"
    entryNumberSusceptible.default = 6
    entryNumberSusceptible.type = "int"
    entryNumberSusceptible.pack(side = TOP)

    # define gridsize x
    labelGridsizeX = tkinter.Label(leftFrame, text = "Gridsize X")
    labelGridsizeX.pack(side = TOP)
    entryGridsizeX = settingEntry(rightFrame)
    entryGridsizeX.variableName = "gridsize_x"
    entryGridsizeX.default = 43
    entryGridsizeX.type = "int"
    entryGridsizeX.pack(side = TOP)

    # define gridsize y
    labelGridsizeY = tkinter.Label(leftFrame, text = "Gridsize Y")
    labelGridsizeY.pack(side = TOP)
    entryGridsizeY = settingEntry(rightFrame)
    entryGridsizeY.variableName = "gridsize_y"
    entryGridsizeY.default = 43
    entryGridsizeY.type = "int"
    entryGridsizeY.pack(side = TOP)

    # define max time
    labelMaxTime = tkinter.Label(leftFrame, text = "Max Time")
    labelMaxTime.pack(side = TOP)
    entryMaxTime = settingEntry(rightFrame)
    entryMaxTime.variableName = "max_time"
    entryMaxTime.default = 30000
    entryMaxTime.type = "int"
    entryMaxTime.pack(side = TOP)

    # define midpoint exposure
    labelMidpointExposure = tkinter.Label(leftFrame, text = "Midpoint Exposure")
    labelMidpointExposure.pack(side = TOP)
    entryMidpointExposure = settingEntry(rightFrame)
    entryMidpointExposure.variableName = "midpoint_exposure"
    entryMidpointExposure.default = 50
    entryMidpointExposure.type = "int"
    entryMidpointExposure.pack(side = TOP)

   

    #define error message
    labelErrorMessage = tkinter.Label(bottomFrame, text = "", fg = "#f00")
    labelErrorMessage.pack(side = TOP)

    # store all entry objects in a list
    entries = [widget for widget in rightFrame.winfo_children() if isinstance(widget, settingEntry)]

    # define save button
    # the save button creates a map containing every setting and value and outputs the map to a JSON file
    settings = {}
    def saveSettings():
        badInput = FALSE
        labelErrorMessage['text'] = ""

        for entry in entries:
            settings[entry.variableName] = entry.get()

            if entry.type == "decimal":
                decimalRemove = settings[entry.variableName].replace(".", "", 1) # remove up to one decimal point. 
                # a valid positive decimal number has up to one decimal and all other characters are digits
                if not decimalRemove.isdigit():
                        badInput = TRUE
                        labelErrorMessage['text'] = str(entry.variableName) + " must be a positive decimal value"
            else: #entry.type is int
                if not settings[entry.variableName].isdigit():
                        badInput = TRUE
                        labelErrorMessage['text'] = str(entry.variableName) + " must be a positive integer value"

        if not badInput:
            outFile = open(folderDirectory + "\\settings.json", "w")
            outFile.write(json.dumps(settings, indent = 0))
            outFile.close()
        
        settingsFrame.destroy()
        # TODO
        # Replace the settings frame with the simulation data


    # define defaults button
    # default button sets all entries to default values and saves these new values to the settings file
    def setAsDefaults():
        for entry in entries:
            entry.delete(0, END)
            entry.insert(0, entry.default)
        saveSettings()

    # read settings from JSON file and display in the text entry forms
    # to be used when the window is opened
    def readSettings():
        # read settings file into a map
        with open(folderDirectory + "\\settings.json") as f:
            settingsIn = json.load(f)
        
        for entry in entries:
            entry.delete(0, END)
            entry.insert(0, settingsIn[entry.variableName])

    def cancel():
        settingsFrame.destroy()
        # TODO
        # Replace the settings frame with the simulation data

    buttonSpecs = [
        #["name", function],
        ["Cancel", cancel],
        ["Save Settings", saveSettings],
        ["Set Default Values", setAsDefaults],
    ]

    Frame_Buttons.buttonBuilder(bottomFrame, buttonSpecs)

    #inialize display of settings
    readSettings()