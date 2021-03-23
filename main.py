import tkinter as tk
from main_page import main_page
from tkinter import ttk

from training_page.training_page import TrainingPage


class DietPage:
    def __init__(self, app):
        super().__init__()
        self.root = app
        self.lframe_find_client = tk.LabelFrame(master=app, labelanchor='nw', text='Jídelníček', padx=10,
                                                pady=10)
        self.test = tk.Label(master=self.lframe_find_client, text="Test")
        self.test.pack()
        self.lframe_find_client.pack()

    def get_main_frame(self):
        return self.lframe_find_client


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Evidence klientů - SMI0114")
    pages = ttk.Notebook(root)

    main_page = main_page.MainPage(root)
    diet_page = DietPage(root)
    training_page = TrainingPage(root)

    first_page = main_page.get_main_frame()
    second_page = diet_page.get_main_frame()
    third_page = training_page.get_main_frame()

    pages.add(first_page, text="Informace o klientovi")
    pages.add(second_page, text="Klientův jídelníček")
    pages.add(third_page, text="Tréninky")

    pages.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
