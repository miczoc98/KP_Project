import tkinter as tk
from tkinter import ttk

from tkinter import font as tkfont
from PlotPage import PlotPage

import matplotlib
matplotlib.use("TkAgg")

LARGE_FONT = 18

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        tk.Tk.wm_title(self, "Fast and Simple Fitting Tool")
        self.geometry("1400x1000")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageGetData, PageTwo, PlotPage):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageGetData)

    def show_frame(self, page):
        '''Show a frame for the given page name'''
        frame = self.frames[page]
        frame.tkraise()

    def show_main_frame(self):
        pass


class PageGetData(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        label = ttk.Label(self, text="GetData", font=LARGE_FONT)
        label.pack(side="top", pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(PageGetData))
        button1.pack()


        button2 = ttk.Button(self, text="Wykres " + "''", command=lambda: controller.show_frame(PlotPage))
        button2.pack()

        button3 = ttk.Button(self, text="SavedCurves", command=lambda: controller.show_frame(PageTwo))
        button3.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        label = ttk.Label(self, text="GetData", font=LARGE_FONT)
        label.pack(side="top", pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(PageGetData))
        button1.pack()

        button2 = ttk.Button(self, text="PageTwo "  + "''", command=lambda: controller.show_frame(PageGetData))
        button2.pack()

        button3 = ttk.Button(self, text="SavedCurves", command=lambda: controller.show_frame(PageGetData))
        button3.pack()

app = App()
app.mainloop()