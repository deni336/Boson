import tkinter as tk
import SettingsPage as SP
import BosonFront as BF


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        mainFrame = tk.Frame(self, bg="#4b4b4b")
        mainFrame.pack_propagate(0)
        mainFrame.pack(fill="both", expand=True)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        self.geometry('90x1060+0+0')
        self.frames = {}
        pages = (BF.BosonFront, SP.SettingsPage)
        for F in pages:
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(BF.BosonFront)
        self.overrideredirect(1)
        self.attributes('-topmost', True)
        menuBar = MenuBar(self)
        tk.Tk.config(self, menu=menuBar)
        
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