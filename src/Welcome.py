import NewSim
import Simulation
import Frame_Buttons
import tkinter
import tkinter.font
from PIL import Image, ImageTk
import os
from tkinter.constants import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory

def welcome(mainFrame, window):

    # ==========================================================
    # define the right frame
    # this is where information is displayed
    rightFrame = tkinter.Frame(mainFrame, borderwidth = 2)
    rightFrame.pack(side = RIGHT)

    # define the Paragraph label
    paragraph = tkinter.Label(rightFrame, justify = LEFT, text = 
    "Lorem ipsum dolor sit amet, consectetur \n"
    "adipiscing elit. Integer vel lacinia \n"
    "metus. Integer nec feugiat odio. Sed eget\n"
    "interdum mauris, sed tincidunt erat. Nunc\n"
    "consequat orci non mi luctus, ut vehicula.\n")
    paragraph.pack(side = BOTTOM)

    # define the Title label
    title = tkinter.Label(rightFrame, text = "Welcome")
    title.pack(side = BOTTOM)

    # define the Title label
    imgFile = Image.open("src\\assets\\scientisthdpi.png")
    imgFile = imgFile.resize((300,250))
    render = ImageTk.PhotoImage(imgFile)
    img = tkinter.Label(rightFrame, image = render)
    img.image = render
    img.pack(side = BOTTOM)

    # ==========================================================
    # define the left frame
    # this is where the start page buttons should be held
    leftFrame = tkinter.Frame(mainFrame, width = 300, height = 300, borderwidth = 2)
    leftFrame.pack_propagate(0)
    leftFrame.pack(side = LEFT)

    # define the new button's function
    def newSim():
        NewSim.newSim(mainFrame, leftFrame, rightFrame)

    # define the open button's function
    def openSim():
        title.config(text = "Open Sim")
        folder = askdirectory()
        #file = askdirectory(mode ='r', filetypes =[('Python Files', '*.txt')])
        if folder is not None:
            leftFrame.destroy()
            rightFrame.destroy()
            print(folder)
            Simulation.simulation(mainFrame, folder)

        

    # define the recent button's function
    def exit():
        window.destroy()


    buttonSpecs = [
        #["name", function],
        ["New Sim", newSim],
        ["Open Sim", openSim],
        ["Exit", exit],
    ]

    Frame_Buttons.buttonBuilder(leftFrame, buttonSpecs)
