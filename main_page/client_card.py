import tkinter as tk
from tkinter import ttk

from main_page.personal_info import PersonalInfo


class ClientCard:
    def __init__(self, root):
        super().__init__()

        # FRAMES
        self.lframe_find_client = tk.LabelFrame(master=root, labelanchor='nw', text='Karta klienta', padx=6,
                                                pady=6)
        self.personal_info = PersonalInfo(self.lframe_find_client)

        self.lframe_find_client.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
