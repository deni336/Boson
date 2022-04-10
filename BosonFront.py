from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import cv2, sys
import GUI as G

#Globals
colorMapDict = {"AUTUMN": cv2.COLORMAP_AUTUMN, "BONE": cv2.COLORMAP_BONE,
                "CIVIDIS": cv2.COLORMAP_CIVIDIS, "COOL": cv2.COLORMAP_COOL,
                "DEEPGREEN": cv2.COLORMAP_DEEPGREEN, "HOT": cv2.COLORMAP_HOT,
                "HSV": cv2.COLORMAP_HSV, "INFERNO": cv2.COLORMAP_INFERNO,
                "JET": cv2.COLORMAP_JET, "MAGMA": cv2.COLORMAP_MAGMA,
                "OCEAN": cv2.COLORMAP_OCEAN, "PARULA": cv2.COLORMAP_PARULA,
                "PINK": cv2.COLORMAP_PINK, "PLASMA": cv2.COLORMAP_PLASMA,
                "RAINBOW": cv2.COLORMAP_RAINBOW, "SPRING": cv2.COLORMAP_SPRING,
                "SUMMER": cv2.COLORMAP_SUMMER, "TURBO": cv2.COLORMAP_TURBO,
                "TWILIGHT": cv2.COLORMAP_TWILIGHT, "TWILIGHT SHIFTED": cv2.COLORMAP_TWILIGHT_SHIFTED,
                "VIRIDIS": cv2.COLORMAP_VIRIDIS, "WINTER": cv2.COLORMAP_WINTER}
currentColorPalette = 14
clicked = "INFERNO"

class BosonFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        utilFrame = LabelFrame(self.mainFrame, G.frameStyles, text="Utilities")
        utilFrame.grid(row=0, column=0, rowspan=100, sticky="n")

        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=3, column=0, pady=2, padx=5)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=4, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=5, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=6, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=7, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=8, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=9, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=10, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=11, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=12, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=13, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=14, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=15, column=0, pady=2)
        btn1 = ttk.Button(utilFrame, text="btn1", command=lambda: sys.exit()).grid(row=16, column=0, pady=2)

        cameraFrame = Frame(self.mainFrame, bg= "#4b4b4b").grid(row=0, column=1)
        lmain = Label(cameraFrame, bg= "#4b4b4b")
        lmain.grid(row=0, column=1)

        cap = cv2.VideoCapture(0)

        def videoStream():
            _, frame = cap.read()
            #frames = cv2.applyColorMap(frame, colormap=cv2.COLORMAP_COOL)
            cv2Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2ImageResize = cv2.resize(cv2Image, (1680, 1005))
            img = Image.fromarray(cv2ImageResize)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, videoStream)
        videoStream()

        colorMapList = ["AUTUMN", "BONE", "CIVIDIS", "COOL", "DEEPGREEN",
                        "HOT", "HSV", "INFERNO", "JET", "MAGMA", "OCEAN", 
                        "PARULA", "PINK", "PLASMA", "RAINBOW", "SPRING",
                        "SUMMER", "TURBO", "TWILIGHT", "TWILIGHT_SHIFTED",
                        "VIRIDIS", "WINTER"]

        clicked = StringVar()
        clicked.set("")
        drop = OptionMenu(utilFrame , clicked , *colorMapList)
        drop.grid(row=0, column=0, pady=2, padx=5)
        button = Button(utilFrame, text="Submit", command=lambda: showColorPaletteLabel()).grid(row=1, column=0, pady=2, padx=5)
        label = Label(utilFrame, bg= "#4b4b4b", text="Palette")
        label.grid(row=2, column=0, pady=2, padx=5) 
        global currentColorPalette
        currentColorPalette = clicked.get()

        def showColorPaletteLabel():
            label.config(text=clicked.get())


    def setColorPalette():
        colorMapNumber = colorMapDict.get(currentColorPalette)
        return colorMapNumber
