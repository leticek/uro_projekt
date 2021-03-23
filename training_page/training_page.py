import tkinter as tk

import multi_listbox as multi_listbox
from training_page.picked_training import PickedTraining
from training_page.planned_training import PlannedTraining


class TrainingPage:
    def __init__(self, app):
        super().__init__()
        self.root = app
        self.lframe_new_training = tk.LabelFrame(master=app, labelanchor='nw', text='Trénink', padx=7,
                                                 pady=7)
        self.lframe_training_history = tk.LabelFrame(master=self.lframe_new_training, labelanchor='nw',
                                                     text='Historie tréninků', padx=7,
                                                     pady=7)
        self.lframe_exercises = tk.LabelFrame(master=self.lframe_new_training, labelanchor='nw',
                                              text='Souhrn', padx=7,
                                              pady=7)
        self.lframe_new_training.rowconfigure(0, weight=1)
        self.lframe_new_training.rowconfigure(1, weight=1)
        self.lframe_new_training.rowconfigure(2, weight=1)

        self.lframe_new_training.columnconfigure(0, weight=1)
        self.lframe_new_training.columnconfigure(1, weight=1)
        self.lframe_new_training.columnconfigure(2, weight=1)

        self.lframe_training_history.columnconfigure(0, weight=1)
        self.lframe_training_history.rowconfigure(0, weight=1)

        self.lframe_exercises.columnconfigure(0, weight=1)
        self.lframe_exercises.rowconfigure(0, weight=1)

        self.mlb_history = multi_listbox.MultiListbox(self.lframe_training_history,
                                                      (('Datum', 8), ('Název', 10), ('Den v týdnu', 7)))
        self.mlb_exercises = multi_listbox.MultiListbox(self.lframe_exercises,
                                                        (('Cvik', 8), ('Série', 10), ('Opakování', 7), ('Zátěž', 7)))

        self.mlb_history.grid(row=0, column=0, sticky=tk.W + tk.E + tk.S + tk.N)
        self.mlb_exercises.grid(row=0, column=0, sticky=tk.W + tk.E + tk.S + tk.N)

        self.lframe_exercises.grid(row=1, column=2, sticky=tk.W + tk.E + tk.S + tk.N)
        self.lframe_training_history.grid(row=0, column=0, sticky=tk.W + tk.E + tk.S + tk.N)
        self.b_save = tk.Button(self.lframe_new_training, text="Uložit").grid(row=2, column=0, columnspan=3,
                                                                              sticky=tk.N + tk.S + tk.E + tk.W)

        self.planned_training = PlannedTraining(main_frame=self.lframe_new_training)
        self.picked_training = PickedTraining(main_frame=self.lframe_new_training)

        self.lframe_new_training.pack()

    def get_main_frame(self):
        return self.lframe_new_training
