import tkinter as tk
from tkinter import ttk
import multi_listbox as multi_listbox


class FindClient:

    def __init__(self, main_frame):
        super().__init__()

        self.lframe_find_client = tk.LabelFrame(master=main_frame, labelanchor='nw', text='Najdi klienta', padx=6,
                                                pady=6)
        for i in range(4):
            self.lframe_find_client.rowconfigure(i, weight=1)

        for i in range(5):
            self.lframe_find_client.columnconfigure(i, weight=1)

        # LABELS
        self.l_personal_number = tk.Label(master=self.lframe_find_client, text="Osobní číslo:").grid(
            sticky=tk.E + tk.N + tk.S)
        self.l_name = tk.Label(master=self.lframe_find_client, text="Jméno:").grid(row=1, sticky=tk.E + tk.N + tk.S)
        self.l_surname = tk.Label(master=self.lframe_find_client, text="Příjmení:").grid(row=2,
                                                                                         sticky=tk.E + tk.N + tk.S)
        self.l_age = tk.Label(master=self.lframe_find_client, text="Věk:").grid(row=0, column=2,
                                                                                sticky=tk.E + tk.N + tk.S)

        # TEXTBOXES
        self.tb_personal_number = tk.Text(master=self.lframe_find_client, width=4, height=1).grid(row=0, column=1,
                                                                                                  sticky=tk.W + tk.E,
                                                                                                  padx=2, pady=2)
        self.tb_name = tk.Text(master=self.lframe_find_client, width=10, height=1).grid(row=1, column=1,
                                                                                        sticky=tk.W + tk.E, padx=2,
                                                                                        pady=2)
        self.tb_surname = tk.Text(master=self.lframe_find_client, width=10, height=1).grid(row=2, column=1,
                                                                                           sticky=tk.W + tk.E, padx=2,
                                                                                           pady=2)

        # LISTBOX
        self.lb_age_values = tk.StringVar()
        self.lb_age = ttk.Combobox(master=self.lframe_find_client, height=1, width=6,
                                   values="1970 1971 1972 1973").grid(row=0, column=3, sticky=tk.W + tk.E)

        # CHECKBOX
        self.cb_active = ttk.Checkbutton(master=self.lframe_find_client, text="Aktivní").grid(row=1, column=2,
                                                                                              columnspan=2)

        # RADIOBUTTONS
        self.rb_man = tk.Radiobutton(master=self.lframe_find_client, text="Muži").grid(row=0, column=4, columnspan=2,
                                                                                       sticky=tk.W + tk.N + tk.S)
        self.rb_woman = tk.Radiobutton(master=self.lframe_find_client, text="Ženy").grid(row=1, column=4, columnspan=2,
                                                                                         sticky=tk.W + tk.N + tk.S)
        self.rb_all = tk.Radiobutton(master=self.lframe_find_client, text="Všichni").grid(row=2, column=4, columnspan=2,
                                                                                          sticky=tk.W + tk.N + tk.S)

        # BUTTONS
        self.b_find_person = tk.Button(master=self.lframe_find_client, text="Hledej").grid(row=3, column=0,
                                                                                           columnspan=6,
                                                                                           sticky=tk.W + tk.E)

        # MULTILISTBOX
        self.multiListBox = multi_listbox.MultiListbox(self.lframe_find_client,
                                                       (('Osobní číslo', 4), ('Jméno', 15), ('Příjmení', 15),
                                                        ('Rok narození', 4)))
        self.multiListBox.grid(row=4, columnspan=5)

        self.lframe_find_client.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
