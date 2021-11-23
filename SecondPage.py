import tkinter as tk
from tkinter import ttk

LARGE_FONT = 18

class SecondPage(tk.Frame):
    name = "Second"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        label = ttk.Label(self, text="Second", font=LARGE_FONT)
        label.pack(side="top", pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Main", command=lambda: controller.show_frame("Main"))
        button1.pack()

        button2 = ttk.Button(self, text="Show Plot", command=lambda: controller.show_frame("Plot"))
        button2.pack()