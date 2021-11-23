import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from PageTwo import PageTwo


class PlotPage(tk.Frame):
    name = "Plot"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        self.width = 2
        self.height = 4

        self.f = Figure(figsize=(10,5), dpi=100)

        self.ax = self.f.add_subplot(111)

        label = ttk.Label(self, text="GraphPage", font=18)
        label.grid(row=0, column=0, columnspan=self.width)

        buttonMenu = ttk.Button(self, text="Back to Main", command=lambda: controller.show_frame("Main"))
        buttonMenu.grid(row=self.height + 2, column=self.width - 2, sticky="nswe")

        buttonDelete = ttk.Button(self, text="Second page", command=lambda: controller.show_frame("Second"))
        buttonDelete.grid(row=self.height + 2, column=self.width - 1, sticky="nswe")

        canvas = FigureCanvasTkAgg(self.f, self)
        canvas.get_tk_widget().grid(row=2, column=0, rowspan=self.height, columnspan=self.width, sticky="nswe")

        self.ax.plot([1, 2, 3, 4, 5],
                     [1, 2, 3, 4, 5], "o", picker=15)
        cid = self.f.canvas.mpl_connect('pick_event', self.on_click)
        
    def on_click(self):
        pass
    
    def delete(self):
        pass
