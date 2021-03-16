import tkinter as tk

from main_page.client_card import ClientCard
from main_page.find_client import FindClient


class MainPage:
    def __init__(self, app):
        super().__init__()
        self.root = app
        self.main_frame = tk.Frame(master=app)
        self.find_client_section = FindClient(self.main_frame)
        self.client_card_section = ClientCard(self.main_frame)

        self.main_frame.pack()

    def get_main_frame(self):
        return self.main_frame
