import tkinter as tk
import threading
import SettingsPage as SP
import FrontEnd as FE

#import CameraEngine as CE

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        mainFrame = tk.Frame(self, bg="#4b4b4b")
        #mainFrame.pack_propagate(0)
        mainFrame.grid(sticky="nesw")
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        #self.geometry('1920x1080+0+0')
        self.state("zoomed")
        self.frames = {}
        pages = (FE.BosonFront, SP.SettingsPage)
        for F in pages:
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(FE.BosonFront) 
        #self.attributes('-topmost', True)
        menuBar = MenuBar(self)
        tk.Tk.config(self, menu=menuBar)

        # videoThread = threading.Thread(target=CE.CameraStream.videoStream())
        # videoThread.start()

    def showFrame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def quitApplication(self):
        self.destroy()


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.quitApplication())

root = MyApp()
root.title("Boson")
root.mainloop()