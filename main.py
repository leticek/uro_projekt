import tkinter as tk
from tkinter import ttk
import multi_listbox as multi_list_box


class MainPage:
    def __init__(self, app) -> None:
        super().__init__()
        self.root = app
        self.main_frame = tk.Frame(master=app)
        self.lframe_find_client = tk.LabelFrame(master=self.main_frame, labelanchor='nw', text='Najdi klienta', padx=6,
                                                pady=6)
        # LABELS
        self.l_personal_number = tk.Label(master=self.lframe_find_client, text="Osobní číslo:")
        self.l_name = tk.Label(master=self.lframe_find_client, text="Jméno:")
        self.l_surname = tk.Label(master=self.lframe_find_client, text="Příjmení:")
        self.l_age = tk.Label(master=self.lframe_find_client, text="Věk:")

        self.l_personal_number.grid(sticky=tk.E + tk.N + tk.S)
        self.l_name.grid(row=1, sticky=tk.E + tk.N + tk.S)
        self.l_surname.grid(row=2, sticky=tk.E + tk.N + tk.S)
        self.l_age.grid(row=0, column=2, sticky=tk.E + tk.N + tk.S)

        # TEXTBOXES
        self.tb_personal_number = tk.Text(master=self.lframe_find_client, width=4, height=1)
        self.tb_name = tk.Text(master=self.lframe_find_client, width=10, height=1)
        self.tb_surname = tk.Text(master=self.lframe_find_client, width=10, height=1)

        self.tb_personal_number.grid(row=0, column=1, sticky=tk.W + tk.N + tk.S, padx=5, pady=5)
        self.tb_name.grid(row=1, column=1, sticky=tk.W + tk.N + tk.S, padx=5, pady=5)
        self.tb_surname.grid(row=2, column=1, sticky=tk.W + tk.N + tk.S, padx=5, pady=5)

        # LISTBOX
        self.lb_age_values = tk.StringVar()
        self.lb_age = ttk.Combobox(master=self.lframe_find_client, height=1, width=6,
                                   values="1970 1971 1972 1973")

        self.lb_age.grid(row=0, column=3, sticky=tk.W + tk.N + tk.S)

        # CHECKBOX
        self.cb_active = ttk.Checkbutton(master=self.lframe_find_client, text="Aktivní")

        self.cb_active.grid(row=1, column=2, columnspan=2)

        # RADIOBUTTONS
        self.rb_man = tk.Radiobutton(master=self.lframe_find_client, text="Muži")
        self.rb_woman = tk.Radiobutton(master=self.lframe_find_client, text="Ženy")
        self.rb_all = tk.Radiobutton(master=self.lframe_find_client, text="Všichni")

        self.rb_man.grid(row=0, column=4, columnspan=2, stick=tk.W + tk.N + tk.S)
        self.rb_woman.grid(row=1, column=4, columnspan=2, stick=tk.W + tk.N + tk.S)
        self.rb_all.grid(row=2, column=4, columnspan=2, stick=tk.W + tk.N + tk.S)

        # BUTTONS
        self.b_find_person = tk.Button(master=self.lframe_find_client, text="Hledej")

        self.b_find_person.grid(row=3, column=0, columnspan=6, sticky=tk.W + tk.E)

        # MULTILISTBOX
        self.multiListBox = multi_list_box.MultiListbox(self.lframe_find_client,
                                                        (('Osobní číslo', 4), ('Jméno', 15), ('Příjmení', 15),
                                                         ('Rok narození', 4)))
        self.multiListBox.grid(row=4, columnspan=5)

        self.lframe_find_client.pack(side=tk.LEFT, fill=tk.Y)

    def getMainFrame(self):
        return self.main_frame


class DietPage:
    def __init__(self, app) -> None:
        super().__init__()
        self.root = app
        self.lframe_find_client = tk.LabelFrame(master=app, labelanchor='nw', text='Jídelníček', padx=10,
                                                pady=10)
        self.test = tk.Label(master=self.lframe_find_client, text="Test")
        self.test.pack()
        self.lframe_find_client.pack()

    def getMainFrame(self):
        return self.lframe_find_client


class TrainingPage:
    def __init__(self, app) -> None:
        super().__init__()
        self.root = app
        self.lframe_find_client = tk.LabelFrame(master=app, labelanchor='nw', text='Trénink', padx=10,
                                                pady=10)
        self.test = tk.Label(master=self.lframe_find_client, text="Test")
        self.test.pack()
        self.lframe_find_client.pack()

    def getMainFrame(self):
        return self.lframe_find_client


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Evidence klientů - SMI0114")
    pages = ttk.Notebook(root)

    main_page = MainPage(root)
    diet_page = DietPage(root)
    training_page = TrainingPage(root)

    first_page = main_page.getMainFrame()
    second_page = diet_page.getMainFrame()
    third_page = training_page.getMainFrame()

    pages.add(first_page, text="Informace o klientovi")
    pages.add(second_page, text="Klientův jídelníček")
    pages.add(third_page, text="Tréninky")

    pages.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
