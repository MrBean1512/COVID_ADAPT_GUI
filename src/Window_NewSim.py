# settings window which is accessed through the main window under open sim
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

def window_NewSim():
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
    labelProjectName = tkinter.Label(leftFrame, text = "Project Name")
    labelProjectName.pack(side = TOP)
    entryProjectName = settingEntry(rightFrame)
    entryProjectName.variableName = "project_name"
    entryProjectName.default = "New_Project"
    entryProjectName.pack(side = TOP)

    # store all entry objects in a list
    entries = [widget for widget in rightFrame.winfo_children() if isinstance(widget, settingEntry)]

    # define back  button
    # closes the settings window and returns to the main window
    backButton = tkinter.Button(bottomFrame, text = "Cancel", command = tk.destroy)
    backButton.pack(side = BOTTOM)

    # define save button
    # the save button creates a map containing every setting and value and outputs the map to a JSON file
    info = {}
    def saveSettings():
        for entry in entries:
            info[entry.variableName] = entry.get()
        print(entries[0].get())


        fileName = "bin\\"+entries[0].get()+"\\projectInfo.json"
        if not os.path.exists(os.path.dirname(fileName)):
            try:
                os.makedirs(os.path.dirname(fileName))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(fileName, "w") as f:
            f.write(str(info))

        #outFile = open("src\\bin\\"+entries[0].get()+"\\projectInfo.json", "w")
        #outFile.write(json.dumps(info))
        #outFile.close()

    saveButton = tkinter.Button(bottomFrame, text = "Create New", command = saveSettings)
    saveButton.pack(side = BOTTOM)

    # display the window
    tk.mainloop()