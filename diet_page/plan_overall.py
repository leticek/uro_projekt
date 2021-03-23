import tkinter as tk


class PlanOverall:

    def __init__(self, master) -> None:
        self.root = tk.LabelFrame(master, text="Parametry plánu", padx=5, pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        self.l_calories = tk.Label(self.root, text="Kalorie: ").grid(row=0, column=0, sticky=tk.E)
        self.l_protein = tk.Label(self.root, text="Bílkoviny: ").grid(row=1, column=0, sticky=tk.E)
        self.l_carbs = tk.Label(self.root, text="Sacharidy: ").grid(row=2, column=0, sticky=tk.E)
        self.l_fat = tk.Label(self.root, text="Tuky: ").grid(row=3, column=0, sticky=tk.E)
        self.l_fibre = tk.Label(self.root, text="Vláknina: ").grid(row=4, column=0, sticky=tk.E)

        self.t_calories = tk.Text(self.root, width=10, height=1).grid(row=0, column=1, sticky=tk.W)
        self.t_protein = tk.Text(self.root, width=10, height=1).grid(row=1, column=1, sticky=tk.W)
        self.t_carbs = tk.Text(self.root, width=10, height=1).grid(row=2, column=1, sticky=tk.W)
        self.t_fat = tk.Text(self.root, width=10, height=1).grid(row=3, column=1, sticky=tk.W)
        self.t_fibre = tk.Text(self.root, width=10, height=1).grid(row=4, column=1, sticky=tk.W)

        self.root.grid(row=2, column=0, sticky=tk.E + tk.W + tk.N + tk.S)
