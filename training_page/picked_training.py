import tkinter as tk
from tkinter import ttk

import multi_listbox


class PickedTraining:

    def __init__(self, main_frame):
        super().__init__()
        self.lframe_planned_training = tk.LabelFrame(master=main_frame, text="Vybraný trénink", pady=7, padx=7)

        for i in range(5):
            self.lframe_planned_training.rowconfigure(i, weight=1)
            self.lframe_planned_training.columnconfigure(i, weight=1)

        self.l_date = tk.Label(self.lframe_planned_training, text="Datum: ").grid(row=0, column=0, sticky=tk.W)
        self.l_place = tk.Label(self.lframe_planned_training, text="Místo: ").grid(row=1, column=0, sticky=tk.W)
        self.l_training_len = tk.Label(self.lframe_planned_training, text="Délka tréninku: ").grid(row=2, column=0,
                                                                                                   sticky=tk.W)
        self.l_focus = tk.Label(self.lframe_planned_training, text="Zaměření: ").grid(row=3, column=0, sticky=tk.W)
        self.l_note = tk.Label(self.lframe_planned_training, text="Poznámka: ").grid(row=4, column=0, sticky=tk.W)
        self.l_time = tk.Label(self.lframe_planned_training, text="Čas: ").grid(row=0, column=2, sticky=tk.W)
        self.lb_time_hours = ttk.Combobox(self.lframe_planned_training, height=1, width=6,
                                          values="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23").grid(
            row=0, column=3, sticky=tk.W)
        self.lb_time_minutes = ttk.Combobox(self.lframe_planned_training, height=1, width=6,
                                            values="0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59").grid(
            row=0, column=4, sticky=tk.W)

        self.lb_place = ttk.Combobox(self.lframe_planned_training, height=1, width=6,
                                     values="Ostrava Karviná Havířov").grid(row=1, column=1, sticky=tk.W + tk.E)
        self.t_training_len = tk.Text(self.lframe_planned_training, height=1, width=7).grid(row=2, column=1,
                                                                                            sticky=tk.W+tk.E, padx=5)
        self.t_focus = tk.Text(self.lframe_planned_training, height=1, width=7).grid(row=3, column=1, sticky=tk.W+tk.E, padx=5)
        self.t_note = tk.Text(self.lframe_planned_training, height=2, width=7, padx=5).grid(row=5, column=0, columnspan=2,
                                                                                    sticky=tk.W + tk.E + tk.S + tk.N)

        self.lframe_training_plan = tk.LabelFrame(self.lframe_planned_training, text="Plán tréninku", pady=7,
                                                  padx=7)
        self.lframe_training_plan.rowconfigure(0, weight=1)
        self.lframe_training_plan.columnconfigure(0, weight=1)

        self.mlb_exercises = multi_listbox.MultiListbox(self.lframe_training_plan,
                                                        (('Cvik', 8), ('Série', 10), ('Opakování', 7),
                                                         ('Zátěž', 7))).grid(row=0,
                                                                             column=0,
                                                                             sticky=tk.W + tk.E + tk.S + tk.N)
        self.lframe_training_plan.grid(row=1, column=2, rowspan=5, columnspan=3,
                                       sticky=tk.W + tk.E + tk.S + tk.N)

        self.lframe_planned_training.grid(row=0, column=1, columnspan=2, sticky=tk.W + tk.E + tk.S + tk.N)
