# settings window which is accessed through the main window under open sim
import Window_Prog
import tkinter 
import tkinter.font
from tkinter.constants import *
from tkinter.filedialog import askopenfile
import json # for reading and writing data
import os   # for file handling
import errno    # error handling

# subclass of Entry that holds the name of the variable in the settings file that the entry corresponds with
class settingEntry(tkinter.Entry):
    def __init__(self, master, *args, **kwargs):
        tkinter.Entry.__init__(self, master, *args, **kwargs)
        self.variableName = "unnamed"
        self.default = ""

def window_NewSim(rightFrame, leftFrame, parent):
    
    # main frame for the new sim function
    newSim = tkinter.Frame(parent)
    newSim.pack(side = TOP)

    # top frame holds left and right frames
    topFrame = tkinter.Frame(newSim)
    topFrame.pack(side = TOP)

    # left frame holds setting names
    labelFrame = tkinter.Frame(topFrame)
    labelFrame.pack(side = LEFT)

    # right frame holds setting entry boxes
    entryFrame = tkinter.Frame(topFrame)
    entryFrame.pack(side = RIGHT)

    # bottom frame holds buttons
    bottomFrame = tkinter.Frame(newSim)
    bottomFrame.pack(side = BOTTOM)

    # define steepness exposure entry
    labelProjectName = tkinter.Label(labelFrame, text = "Project Name")
    labelProjectName.pack(side = TOP)
    entryProjectName = settingEntry(entryFrame)
    entryProjectName.variableName = "project_name"
    entryProjectName.default = "New_Project"
    entryProjectName.pack(side = TOP)

    # store all entry objects in a list
    entries = [widget for widget in entryFrame.winfo_children() if isinstance(widget, settingEntry)]

    # define back  button
    # closes the settings window and returns to the main window
    backButton = tkinter.Button(bottomFrame, text = "Cancel", command = newSim.destroy)
    backButton.pack(side = BOTTOM)

    # define save button
    # the save button creates a map containing every setting and value and outputs the map to a JSON file
    info = {}
    def createNewProject():
        for entry in entries:
            info[entry.variableName] = entry.get()
        print(entries[0].get())
        
        # make a new folder in the saves folder
        fileName = entries[0].get()
        filePath = "saves\\" + fileName + "\\projectInfo.json"
        if not os.path.exists(os.path.dirname(filePath)):
            try:
                os.makedirs(os.path.dirname(filePath))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filePath, "w") as f:
            f.write(str(info))

        leftFrame.destroy()
        rightFrame.destroy()
        newSim.destroy()
        Window_Prog.window_Prog(parent, (os.getcwd() + "\\saves\\" + fileName) )

    saveButton = tkinter.Button(bottomFrame, text = "Create New", command = createNewProject)
    saveButton.pack(side = BOTTOM)

    # display the window
    parent.mainloop()