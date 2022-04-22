from tkinter import LabelFrame
from tkinter import ttk
import re
from CameraEngine import CameraOperations
from FrontEnd import BosonFront
import GUI as G

class ButtonMaster(G.GUI):
    def __init__(self, parent) -> None:

        G.GUI.__init__(self, parent)
        #Utility frame for buttons
        utilFrame = LabelFrame(self, G.frameStyles, text="Utilities")
        utilFrame.grid(row=0, column=0, sticky="nw")
        # frame for displaying temp // for later use
        tempDisplayFrame = LabelFrame(self,self, G.frameStyles, text="Temp")
        tempDisplayFrame.grid(row=1, column=0)
        # Loop for creating buttons
        btnGroup = ["snapShot", "startScreenRecord", "stopScreenRecord", "forceFFC"]
        rowPlus = 2
        for btn in btnGroup:
            btnCom = "CameraOperations." + btn + "()"
            textGroup = [s for s in re.split("([A-Z][^A-Z]*)", btn) if s]
            btnText = ''
            for text in textGroup:
                btnText += text.title() + " "
            btnText.strip()
            rowPlus += 1
            btn = ttk.Button(utilFrame, text=btnText, command=lambda: btnCom).grid(row=rowPlus, column=0, pady=2)