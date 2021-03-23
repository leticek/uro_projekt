import tkinter as tk


class PlanParameters:

    def __init__(self, master) -> None:
        self.root = tk.LabelFrame(master, text="Parametry plánu", padx=5, pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        self.l_start = tk.Label(self.root, text="Začátek: ").grid(row=0, column=0, sticky=tk.E)
        self.l_end = tk.Label(self.root, text="Konec: ").grid(row=1, column=0, sticky=tk.E)
        self.l_weight_before = tk.Label(self.root, text="Váha před: ").grid(row=2, column=0, sticky=tk.E)
        self.l_weight_after = tk.Label(self.root, text="Váha po: ").grid(row=3, column=0, sticky=tk.E)

        self.t_start = tk.Text(self.root, width=10, height=1).grid(row=0, column=1, sticky=tk.W)
        self.t_end = tk.Text(self.root, width=10, height=1).grid(row=1, column=1, sticky=tk.W)
        self.t_weight_before = tk.Text(self.root, width=10, height=1).grid(row=2, column=1, sticky=tk.W)
        self.t_weight_after = tk.Text(self.root, width=10, height=1).grid(row=3, column=1, sticky=tk.W)

        self.lframe_category = tk.LabelFrame(self.root, text="Kategorie")

        for i in range(3):
            self.lframe_category.rowconfigure(i, weight=1)
            self.lframe_category.columnconfigure(i, weight=1)

        self.cb_vegn = tk.Checkbutton(self.lframe_category, text="Vegan").grid(row=0, column=0, sticky=tk.W + tk.E)
        self.cb_keto = tk.Checkbutton(self.lframe_category, text="Keto-dieta").grid(row=1, column=0, sticky=tk.W + tk.E)
        self.cb_dieta = tk.Checkbutton(self.lframe_category, text="Dieta").grid(row=2, column=0, sticky=tk.W + tk.E)
        self.cb_vegetarian = tk.Checkbutton(self.lframe_category, text="Vegetarián").grid(row=0, column=1,
                                                                                          sticky=tk.W + tk.E)
        self.cb_carb_waves = tk.Checkbutton(self.lframe_category, text="Sacharidové vlny").grid(row=1, column=1,
                                                                                                sticky=tk.W + tk.E)
        self.cb_volume = tk.Checkbutton(self.lframe_category, text="Objem").grid(row=2, column=1, sticky=tk.W + tk.E)

        self.lframe_category.grid(row=4, column=0, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.root.grid(row=1, column=0, sticky=tk.E + tk.W + tk.N + tk.S)
