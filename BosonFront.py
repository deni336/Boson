from tkinter import *
from tkinter import ttk
from turtle import width
import sys
import GUI as G
import _thread
import CameraViewer as FCV

class BosonFront(G.GUI):

    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        frame1 = LabelFrame(self.mainFrame, G.frameStyles, text="Utilities")
        frame1.pack(fill="both", expand=True)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=0, column=0, pady=2, padx=5)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=1, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=2, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=3, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=4, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=5, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=6, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=7, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=8, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=9, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=10, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=11, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=12, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=13, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=14, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=15, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=16, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=17, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=18, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=19, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=20, column=0, pady=2)

        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=21, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=22, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=23, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=24, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=25, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=26, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=27, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=28, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=29, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=30, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=31, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=32, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=33, column=0, pady=2)
        btn1 = ttk.Button(frame1, text="btn1", command=lambda: sys.exit()).grid(row=34, column=0, pady=2)


        # def scanning():
        #     if running:  # Only do this if the Stop button has not been clicked
        #         print "hello"

        #     # After 1 second, call scanning again (create a recursive loop)
        #     root.after(1000, scanning)

        # def start():
        #     """Enable scanning by setting the global flag to True."""
        #     global running
        #     running = True

        # def stop():
        #     """Stop scanning by setting the global flag to False."""
        #     global running
        #     running = False
        self.after(50, lambda: _thread.start_new_thread(FCV.startStream(), ("Thread-1", 2, )))


        

