import tkinter as tk
from tkinter import ttk

from tkinter import font as tkfont
from PlotPage import PlotPage
from MainPage import MainPage
from SecondPage import SecondPage

import matplotlib

matplotlib.use("TkAgg")

LARGE_FONT = 18


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        tk.Tk.wm_title(self, "Weather station")
        self.geometry("800x600")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, SecondPage, PlotPage):
            frame = F(container, self)
            self.frames[F.name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Main")

    def show_frame(self, page):
        '''Show a frame for the given page name'''
        frame = self.frames[page]
        frame.tkraise()


app = App()
app.mainloop()
