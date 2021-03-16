import tkinter as tk


class MainPage:
    def __init__(self, master) -> None:
        super().__init__()
        self.root = master
        self.lframe_find_client = tk.LabelFrame(master=self.root, labelanchor="nw")
        self.lframe_find_client.pack()

