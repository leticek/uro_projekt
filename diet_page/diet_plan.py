import tkinter as tk

from diet_page.food_window import FoodWindow


class DietPlan:

    def __init__(self, master) -> None:
        self.root = tk.LabelFrame(master, text="Jídelní plán")

        for i in range(2):
            self.root.rowconfigure(i, weight=1)
        for i in range(2):
            self.root.columnconfigure(i, weight=1)

        self.breakfest = FoodWindow(master=self.root, name="Snídaně", row=0, column=0)
        self.lunch = FoodWindow(master=self.root, name="Oběd", row=0, column=1)
        self.dinner = FoodWindow(master=self.root, name="Večeře", row=0, column=2)
        self.smack_one = FoodWindow(master=self.root, name="Svačina 1", row=1, column=0)
        self.snack_two = FoodWindow(master=self.root, name="Svačina 2", row=1, column=1)
        self.dinner_two = FoodWindow(master=self.root, name="Před spaním", row=1, column=2)

        self.root.grid(row=1, column=1, rowspan=2, columnspan=3, sticky=tk.E + tk.W + tk.N + tk.S)
