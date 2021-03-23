import tkinter as tk


class ClientInfo:

    def __init__(self, master) -> None:
        self.root = tk.LabelFrame(master, text="Informace o klientovi")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        for i in range(5):
            self.root.rowconfigure(i, weight=1)

        self.l_gender = tk.Label(self.root, text="Pohlaví: ").grid(row=0, column=0,
                                                                   sticky=tk.N + tk.E )
        self.l_weight = tk.Label(self.root, text="Váha: ").grid(row=1, column=0,
                                                                sticky=tk.N + tk.E )
        self.l_age = tk.Label(self.root, text="Věk: ").grid(row=2, column=0,
                                                            sticky=tk.N + tk.E )
        self.l_occupation = tk.Label(self.root, text="Zaměstnání: ").grid(row=3, column=0,
                                                                          sticky=tk.N + tk.E )
        self.l_goal = tk.Label(self.root, text="Cíl: ").grid(row=4, column=0,
                                                             sticky=tk.N + tk.E )

        self.t_gender = tk.Text(self.root, width=10, height=1).grid(row=0, column=1,
                                                                    sticky=tk.N + tk.W)
        self.t_weight = tk.Text(self.root, width=10, height=1).grid(row=1, column=1,
                                                                    sticky=tk.N + tk.W)
        self.t_age = tk.Text(self.root, width=10, height=1).grid(row=2, column=1,
                                                                 sticky=tk.N + tk.W)
        self.t_occupation = tk.Text(self.root, width=10, height=1).grid(row=3, column=1,
                                                                        sticky=tk.N + tk.W)
        self.t_goal = tk.Text(self.root, width=10, height=1).grid(row=4, column=1,
                                                                  sticky=tk.N + tk.W)

        self.root.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)
