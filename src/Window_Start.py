import Window_Prog
import Button_Builder
import tkinter
import tkinter.font
from PIL import Image, ImageTk
from tkinter.constants import *
from tkinter.filedialog import askopenfile

def window_Start():

    # define the main frame/window
    #window = tkinter.Frame(parent, relief=RIDGE, borderwidth=2)
    #window.pack(fill=BOTH, expand=1)

    tk = tkinter.Tk()
    tk.title("COVID ADAPT")

    # ==========================================================
    # define the right frame
    # this is where information is displayed
    rightFrame = tkinter.Frame(tk, borderwidth = 2)
    rightFrame.pack(side = RIGHT)

    # define the Title label
    title = tkinter.Label(rightFrame, text = "Welcome")
    title.pack(fill = X, expand = 1)

    # define the Paragraph label
    title = tkinter.Label(rightFrame, justify = LEFT, text = 
    "Thanks for reading this but there's no \n"
     "need to continue looking at this part. \n"
     "People reading my work makes me genuinely \n"
     "uncomfortable. No more, thx.")
    title.pack(fill = X, expand = 1)

    # define the Title label
    imgFile = Image.open("C:\\Users\\mrbea\\Documents\\Whitworth-Visual-Studio\\COVID_ADAPT_GUI\\COVID_ADAPT_GUI\\src\\assets\\scientisthdpi.png")
    imgFile = imgFile.resize((300,250))
    render = ImageTk.PhotoImage(imgFile)
    img = tkinter.Label(rightFrame, image = render)
    img.image = render
    img.pack(fill = X, expand = 1)

    # ==========================================================
    # define the left frame
    # this is where the start page buttons should be held
    leftFrame = tkinter.Frame(tk, width = 300, height = 300, borderwidth = 2)
    leftFrame.pack_propagate(0)
    leftFrame.pack(side = LEFT)

    # define the new button's function
    def newSim():
        title.config(text = "New Sim")

    # define the open button's function
    def openSim():
        title.config(text = "Open Sim")
        file = askopenfile(mode ='r', filetypes =[('Python Files', '*.txt')])
        if file is not None:
            content = file.read()
            print(content)
            title.config(text = content)
        tk.destroy()
        Window_Prog.window_Prog()

    # define the recent button's function
    def recentSim():
        title.config(text = "Recent Sim")


    buttonSpecs = [
        #["name", function],
        ["New Sim", newSim],
        ["Open Sim", openSim],
        ["Recent Sim", recentSim],
    ]

    Button_Builder.buttonBuilder(leftFrame, buttonSpecs)

    # display the tkinter window
    tk.mainloop()