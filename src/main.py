import tkinter as tk
from tkinter.constants import *
import Welcome

# define the main frame/window
window = tk.Tk()
window.title("COVID ADAPT")

window.iconbitmap('./src/assets/covidAdaptLogo.ico')

mainFrame = tk.Frame(window)
mainFrame.pack()

Welcome.welcome(mainFrame, window)

# display the tkinter window
window.mainloop()