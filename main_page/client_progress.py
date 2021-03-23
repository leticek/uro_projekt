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

        for i in range(1):
            self.lframe_start.columnconfigure(i, weight=1)
            self.lframe_actual.columnconfigure(i, weight=1)

        for i in range(2):
            self.lframe_start.rowconfigure(i, weight=1)
            self.lframe_actual.rowconfigure(i, weight=1)

        self.l_start_weight = tk.Label(self.lframe_start, text="Váha:").grid(row=0, column=0, sticky=tk.E)
        self.l_start_fat = tk.Label(self.lframe_start, text="% tuku:").grid(row=1, column=0, sticky=tk.E)
        self.l_start_chest = tk.Label(self.lframe_start, text="Obvod paže:").grid(row=2, column=0, sticky=tk.E)

        self.t_start_weight = tk.Text(self.lframe_start, width=6, height=1).grid(row=0, column=1, sticky=tk.W)
        self.t_start_fat = tk.Text(self.lframe_start, width=6, height=1).grid(row=1, column=1, sticky=tk.W)
        self.t_start_chest = tk.Text(self.lframe_start, width=6, height=1).grid(row=2, column=1, sticky=tk.W)

        self.t_actual_weight = tk.Text(self.lframe_actual, width=6, height=1).grid(row=0, column=1, sticky=tk.E)
        self.t_actual_fat = tk.Text(self.lframe_actual, width=6, height=1).grid(row=1, column=1, sticky=tk.E)
        self.t_actual_chest = tk.Text(self.lframe_actual, width=6, height=1).grid(row=2, column=1, sticky=tk.E)

        self.l_actual_weight = tk.Label(self.lframe_actual, text="Váha:").grid(row=0, column=0, sticky=tk.W)
        self.l_actual_fat = tk.Label(self.lframe_actual, text="% tuku:").grid(row=1, column=0, sticky=tk.W)
        self.l_actual_chest = tk.Label(self.lframe_actual, text="Obvod paže:").grid(row=2, column=0, sticky=tk.W)

        self.lframe_start.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.lframe_actual.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.lframe_client_card.pack(fill=tk.BOTH, expand=True)
