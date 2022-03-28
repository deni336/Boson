import tkinter as tk
import cv2
from PIL import ImageTk, Image
import GUI as G
import OpenCV as CV

class BosonFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Camera Viewer", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Camera Output")
        frame1.place(rely=0.05, relx=0.01, height=820, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Func")
        frame2.place(rely=0.05, relx=0.45, height=200, width=200)


