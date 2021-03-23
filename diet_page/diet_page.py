import tkinter as tk

from diet_page.client_info import ClientInfo


class DietPage:
    def __init__(self, app):
        super().__init__()
        self.root = app
        self.lframe_find_client = tk.LabelFrame(master=app, labelanchor='nw', text='Jídelníček', padx=10,
                                                pady=10)
        for i in range(4):
            self.lframe_find_client.rowconfigure(i, weight=1)
            self.lframe_find_client.columnconfigure(i, weight=1)

        self.client_info = ClientInfo(master=self.lframe_find_client)
        self.plan_parameters = 0
        self.plan_overall = 0
        self.history = 0
        self.picked_overall = 0
        self.diet_plan = 0
        self.vitamins = 0

        self.b_save = tk.Button(self.lframe_find_client, text="Uložit").grid(row=4, column=0, columnspan=4,
                                                                             sticky=tk.N + tk.E + tk.S + tk.W)

        self.lframe_find_client.pack()

    def get_main_frame(self):
        return self.lframe_find_client
