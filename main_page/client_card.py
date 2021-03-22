import tkinter as tk

from main_page.client_progress import ClientProgress
from main_page.personal_info import PersonalInfo


class ClientCard:
    def __init__(self, root):
        super().__init__()

        # FRAMES
        self.lframe_client_card = tk.LabelFrame(master=root, labelanchor='nw', text='Karta klienta', padx=6,
                                                pady=6)
        self.personal_info = PersonalInfo(self.lframe_client_card)
        self.client_progress = ClientProgress(self.lframe_client_card)

        self.lframe_client_card.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
