import tkinter as tk
from tkinter import ttk


class PersonalInfo:
    def __init__(self, root) -> None:
        super().__init__()
        # NOTEBOOK
        self.pages = ttk.Notebook(master=root)

        # FRAMES
        self.f_main_client_info = tk.Frame(master=self.pages)
        self.f_other_client_info = tk.Frame(master=self.pages)

        self.f_main_client_info.pack()
        self.f_other_client_info.pack()
        # LABELS
        self.l_title = tk.Label(master=self.f_main_client_info, text="Titul:")
        self.l_name = tk.Label(master=self.f_main_client_info, text="Jméno:")
        self.l_surname = tk.Label(master=self.f_main_client_info, text="Příjmení:")
        self.l_birth_date = tk.Label(master=self.f_main_client_info, text="Datum narození:")
        self.l_occupation = tk.Label(master=self.f_main_client_info, text="Zaměstnání:")

        self.l_phone = tk.Label(master=self.f_other_client_info, text="Telefon:")
        self.l_email = tk.Label(master=self.f_other_client_info, text="Email:")
        self.l_street = tk.Label(master=self.f_other_client_info, text="Ulice:")
        self.l_house_number = tk.Label(master=self.f_other_client_info, text="Číslo popisné:")
        self.l_town = tk.Label(master=self.f_other_client_info, text="Město:")
        self.l_zip_code = tk.Label(master=self.f_other_client_info, text="PSČ:")

        self.l_title.grid(sticky=tk.E)
        self.l_name.grid(sticky=tk.E)
        self.l_surname.grid(sticky=tk.E)
        self.l_birth_date.grid(sticky=tk.E)
        self.l_occupation.grid(sticky=tk.E)

        self.l_phone.grid(row=0, column=1, sticky=tk.E, padx=2, pady=2)
        self.l_email.grid(row=1, column=1, sticky=tk.E, padx=2, pady=2)
        self.l_street.grid(row=2, column=1, sticky=tk.E, padx=2, pady=2)
        self.l_house_number.grid(row=3, column=1, sticky=tk.E, padx=2, pady=2)
        self.l_town.grid(row=4, column=1, sticky=tk.E, padx=2, pady=2)
        self.l_zip_code.grid(row=5, column=1, sticky=tk.E, padx=2, pady=2)

        # TEXTBOXES
        self.tb_title = tk.Text(master=self.f_main_client_info, width=6, height=1)
        self.tb_name = tk.Text(master=self.f_main_client_info, width=10, height=1)
        self.tb_surname = tk.Text(master=self.f_main_client_info, width=10, height=1)
        self.tb_occupation = tk.Text(master=self.f_main_client_info, width=10, height=1)

        self.tb_phone = tk.Text(master=self.f_other_client_info, width=13, height=1)
        self.tb_email = tk.Text(master=self.f_other_client_info, width=20, height=1)
        self.tb_street = tk.Text(master=self.f_other_client_info, width=20, height=1)
        self.tb_house_number = tk.Text(master=self.f_other_client_info, width=7, height=1)
        self.tb_town = tk.Text(master=self.f_other_client_info, width=20, height=1)
        self.tb_zip_code = tk.Text(master=self.f_other_client_info, width=6, height=1)

        self.tb_title.grid(row=0, column=1, sticky=tk.W + tk.N + tk.S, padx=2, pady=2)
        self.tb_name.grid(row=1, column=1, sticky=tk.W + tk.N + tk.S, padx=2, pady=2)
        self.tb_surname.grid(row=2, column=1, sticky=tk.W + tk.N + tk.S, padx=2, pady=2)
        self.tb_occupation.grid(row=4, column=1, sticky=tk.W + tk.N + tk.S, padx=2, pady=2)

        self.tb_phone.grid(row=0, column=2, sticky=tk.W, padx=2, pady=2)
        self.tb_email.grid(row=1, column=2, sticky=tk.W, padx=2, pady=2)
        self.tb_street.grid(row=2, column=2, sticky=tk.W, padx=2, pady=2)
        self.tb_house_number.grid(row=3, column=2, sticky=tk.W, padx=2, pady=2)
        self.tb_town.grid(row=4, column=2, sticky=tk.W, padx=2, pady=2)
        self.tb_zip_code.grid(row=5, column=2, sticky=tk.W, padx=2, pady=2)


        # PAGES
        self.first_page = self.f_main_client_info
        self.second_page = self.f_other_client_info

        self.pages.add(self.first_page, text="Základní informace")
        self.pages.add(self.second_page, text="Adresa")

        self.pages.pack(fill=tk.X)
