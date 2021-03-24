import tkinter as tk

from diet_page.food_window import FoodWindow


class PickedDietPlan:

    def __init__(self, master) -> None:
        self.root = tk.LabelFrame(master, text="Vybraný plán")

        for i in range(2):
            self.root.rowconfigure(i, weight=1)
        for i in range(3):
            self.root.columnconfigure(i, weight=1)

        self.f_overall = tk.Frame(self.root)

        for i in range(5):
            self.f_overall.rowconfigure(i, weight=1)
        for i in range(3):
            self.f_overall.columnconfigure(i, weight=1)

        self.l_start = tk.Label(self.f_overall, text="Začátek: ").grid(row=0, column=0, sticky=tk.E)
        self.l_end = tk.Label(self.f_overall, text="Konec: ").grid(row=1, column=0, sticky=tk.E)
        self.l_weight_before = tk.Label(self.f_overall, text="Váha před: ").grid(row=2, column=0, sticky=tk.E)
        self.l_weight_after = tk.Label(self.f_overall, text="Váha po: ").grid(row=3, column=0, sticky=tk.E)

        self.t_start = tk.Text(self.f_overall, width=10, height=1).grid(row=0, column=1, sticky=tk.W)
        self.t_end = tk.Text(self.f_overall, width=10, height=1).grid(row=1, column=1, sticky=tk.W)
        self.t_weight_before = tk.Text(self.f_overall, width=10, height=1).grid(row=2, column=1, sticky=tk.W)
        self.t_weight_after = tk.Text(self.f_overall, width=10, height=1).grid(row=3, column=1, sticky=tk.W)

        self.f_overall.grid(row=0, column=0, rowspan=3, sticky=tk.E + tk.W + tk.N + tk.S)

        self.breakfest = FoodWindow(master=self.root, name="Snídaně", row=0, column=1)
        self.lunch = FoodWindow(master=self.root, name="Oběd", row=0, column=2)
        self.dinner = FoodWindow(master=self.root, name="Večeře", row=0, column=3)
        self.smack_one = FoodWindow(master=self.root, name="Svačina 1", row=1, column=1)
        self.snack_two = FoodWindow(master=self.root, name="Svačina 2", row=1, column=2)
        self.dinner_two = FoodWindow(master=self.root, name="Před spaním", row=1, column=3)

        self.root.grid(row=0, column=2, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)
