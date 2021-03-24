import tkinter as tk

import multi_listbox
from diet_page.client_info import ClientInfo
from diet_page.diet_plan import DietPlan
from diet_page.picked_diet_plan import PickedDietPlan
from diet_page.plan_overall import PlanOverall
from diet_page.plan_parameters import PlanParameters


class DietPage:
    def __init__(self, master):
        super().__init__()

        self.lframe_main = tk.LabelFrame(master=master, labelanchor='nw', text='Jídelníček', padx=10,
                                         pady=10)
        for i in range(4):
            self.lframe_main.rowconfigure(i, weight=1)
            self.lframe_main.columnconfigure(i, weight=1)

        self.client_info = ClientInfo(master=self.lframe_main)
        self.plan_parameters = PlanParameters(master=self.lframe_main)
        self.plan_overall = PlanOverall(master=self.lframe_main)

        self.lframe_history = tk.LabelFrame(self.lframe_main, text="Historie")
        self.multiListBox = multi_listbox.MultiListbox(self.lframe_history,
                                                       (('Začátek', 4), ('Startovní váha', 15), ('Cílová váha', 15),
                                                        ('Kategorie', 4)))
        self.lframe_history.rowconfigure(0, weight=1)
        self.lframe_history.columnconfigure(0, weight=1)
        self.multiListBox.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
        self.lframe_history.grid(row=0, column=1, sticky=tk.N + tk.E + tk.S + tk.W)

        self.picked_overall = PickedDietPlan(master=self.lframe_main)
        self.diet_plan = DietPlan(master=self.lframe_main)
        self.vitamins = 0

        self.b_save = tk.Button(self.lframe_main, text="Uložit").grid(row=4, column=0, columnspan=4,
                                                                      sticky=tk.N + tk.E + tk.S + tk.W)

        self.lframe_main.pack()

    def get_main_frame(self):
        return self.lframe_main
