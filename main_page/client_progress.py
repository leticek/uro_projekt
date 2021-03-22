import tkinter as tk
from tkinter import ttk


class ClientProgress:
    def __init__(self, root):
        super().__init__()

        # FRAMES
        self.lframe_client_card = tk.LabelFrame(master=root, labelanchor='nw', text='Průběh spolupráce', padx=6,
                                                pady=6)

        self.lframe_start = tk.LabelFrame(self.lframe_client_card, labelanchor='nw', text='Začátek', padx=6,
                                          pady=6)
        self.lframe_actual = tk.LabelFrame(self.lframe_client_card, labelanchor='nw', text='Aktuálně', padx=6,
                                           pady=6)

        self.lframe_start.columnconfigure(0, weight=1)
        self.lframe_start.columnconfigure(1, weight=1)
        self.lframe_start.rowconfigure(0, weight=1)
        self.lframe_start.rowconfigure(1, weight=1)
        self.lframe_start.rowconfigure(2, weight=1)

        self.lframe_actual.columnconfigure(0, weight=1)
        self.lframe_actual.columnconfigure(1, weight=1)
        self.lframe_actual.rowconfigure(0, weight=1)
        self.lframe_actual.rowconfigure(1, weight=1)
        self.lframe_actual.rowconfigure(2, weight=1)

        self.l_start_weight = tk.Label(self.lframe_start, text="Váha:")
        self.l_start_fat = tk.Label(self.lframe_start, text="% tuku:")
        self.l_start_chest = tk.Label(self.lframe_start, text="Obvod paže:")

        self.t_start_weight = tk.Text(self.lframe_start, width=6, height=1)
        self.t_start_fat = tk.Text(self.lframe_start, width=6, height=1)
        self.t_start_chest = tk.Text(self.lframe_start, width=6, height=1)

        self.t_actual_weight = tk.Text(self.lframe_actual, width=6, height=1)
        self.t_actual_fat = tk.Text(self.lframe_actual, width=6, height=1)
        self.t_actual_chest = tk.Text(self.lframe_actual, width=6, height=1)

        self.l_start_weight.grid(row=0, column=0, sticky=tk.E)
        self.l_start_fat.grid(row=1, column=0, sticky=tk.E)
        self.l_start_chest.grid(row=2, column=0, sticky=tk.E)

        self.t_start_weight.grid(row=0, column=1, sticky=tk.W)
        self.t_start_fat.grid(row=1, column=1, sticky=tk.W)
        self.t_start_chest.grid(row=2, column=1, sticky=tk.W)

        self.t_actual_weight.grid(row=0, column=1, sticky=tk.W)
        self.t_actual_fat.grid(row=1, column=1, sticky=tk.W)
        self.t_actual_chest.grid(row=2, column=1, sticky=tk.W)

        self.l_actual_weight = tk.Label(self.lframe_actual, text="Váha:")
        self.l_actual_fat = tk.Label(self.lframe_actual, text="% tuku:")
        self.l_actual_chest = tk.Label(self.lframe_actual, text="Obvod paže:")

        self.l_actual_weight.grid(row=0, column=0, sticky=tk.E)
        self.l_actual_fat.grid(row=1, column=0, sticky=tk.E)
        self.l_actual_chest.grid(row=2, column=0, sticky=tk.E)

        self.lframe_start.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.lframe_actual.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.lframe_client_card.pack(fill=tk.BOTH, expand=True)
