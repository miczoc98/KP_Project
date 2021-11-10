# class PageTwo(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.contoller = controller
#         label = ttk.Label(self, text="GetData", font=LARGE_FONT)
#         label.pack(side="top", pady=10, padx=10)
#
#         button1 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame(PageGetData))
#         button1.pack()
#
#         button2 = ttk.Button(self, text="PageTwo "  + "''", command=lambda: controller.show_frame(PageGetData))
#         button2.pack()
#
#         button3 = ttk.Button(self, text="SavedCurves", command=lambda: controller.show_frame(PageGetData))
#         button3.pack()