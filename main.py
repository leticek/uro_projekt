import tkinter as tk
from tkinter import ttk

from data import clients
from models.klient import Client
from multi_listbox import MultiListbox

if __name__ == '__main__':

    def find_client():
        client_id = t_fc_id.get()
        name = t_fc_name.get()
        surname = t_fc_surname.get()
        age = cb_fc_age.get()
        mlb_clients.delete(0, 10)

        for c in clients:
            if c.client_id == client_id or name in c.name or surname in c.surname or age == c.age or gender.get() == c.gender or active.get() == c.active:
                mlb_clients.insert(tk.END, (c.client_id, c.name, c.surname, c.age))


    current_client = 0


    def choose_client(row):
        global current_client

        if len(t_ci_name.get()) > 0:
            clients[current_client] = Client(client_id=clients[current_client].client_id,
                                             occupation=t_ci_occupation.get(), a_arm=t_ci_a_arm.get(),
                                             s_arm=t_ci_s_arm.get(), s_weight=t_ci_s_weight.get(),
                                             a_weight=t_ci_a_weight.get(), title=t_ci_title.get(),
                                             s_fat=t_ci_s_fat.get(), a_fat=t_ci_a_fat.get(), surname=t_ci_surname.get(),
                                             age=t_ci_age)

        current_client = row

        chosen_client = clients[row]
        t_ci_title.delete(0, "end")
        t_ci_name.delete(0, "end")
        t_ci_surname.delete(0, "end")
        t_ci_age.delete(0, "end")
        t_ci_occupation.delete(0, "end")

        t_ci_phone.delete(0, "end")
        t_ci_email.delete(0, "end")
        t_ci_street.delete(0, "end")
        t_ci_house_number.delete(0, "end")
        t_ci_town.delete(0, "end")
        t_ci_zip.delete(0, "end")

        t_ci_a_weight.delete(0, "end")
        t_ci_a_fat.delete(0, "end")
        t_ci_a_arm.delete(0, "end")
        t_ci_s_weight.delete(0, "end")
        t_ci_s_fat.delete(0, "end")
        t_ci_s_arm.delete(0, "end")

        t_ci_a_weight.insert(0, chosen_client.a_weight)
        t_ci_a_fat.insert(0, chosen_client.a_fat)
        t_ci_a_arm.insert(0, chosen_client.a_arm)
        t_ci_s_weight.insert(0, chosen_client.s_weight)
        t_ci_s_fat.insert(0, chosen_client.s_fat)
        t_ci_s_arm.insert(0, chosen_client.s_arm)

        t_ci_title.insert(0, chosen_client.title)
        t_ci_name.insert(0, chosen_client.name)
        t_ci_surname.insert(0, chosen_client.surname)
        t_ci_age.insert(0, chosen_client.age)
        t_ci_occupation.insert(0, chosen_client.occupation)

        t_ci_phone.insert(0, chosen_client.address.phone)
        t_ci_email.insert(0, chosen_client.address.email)
        t_ci_street.insert(0, chosen_client.address.street)
        t_ci_house_number.insert(0, chosen_client.address.house_number)
        t_ci_town.insert(0, chosen_client.address.town)
        t_ci_zip.insert(0, chosen_client.address.zip_code)


    root = tk.Tk()
    root.wm_title("Evidence klientů - SMI0114")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    main_pages = ttk.Notebook(root)

    gender = tk.IntVar()
    active = tk.IntVar()
    active_client = clients[0]

    # FIRST PAGE
    f_first_page = tk.Frame()

    for i in range(3):
        f_first_page.rowconfigure(i, weight=1)
        f_first_page.columnconfigure(i, weight=1)

    mlb_clients = MultiListbox(f_first_page, (('Osobní číslo', 4), ('Jméno', 15), ('Příjmení', 15), ('Věk', 4)))
    mlb_clients.subscribe(lambda row: choose_client(row))
    mlb_clients.grid(row=2, column=0, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)

    for c in clients:
        mlb_clients.insert(tk.END, (c.client_id, c.name, c.surname, c.age))

    # FIND CLIENT
    lf_find_client = tk.LabelFrame(master=f_first_page, text="Vyhledání klienta")
    for i in range(3):
        lf_find_client.rowconfigure(i, weight=1)
        lf_find_client.columnconfigure(i, weight=1)

    # FIND CLIENT LABELS
    tk.Label(master=lf_find_client, text="Osobní číslo:").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_find_client, text="Jméno:").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_find_client, text="Příjmení:").grid(row=2, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_find_client, text="Věk:").grid(row=0, column=2, sticky=tk.N + tk.W + tk.S)

    # FIND CLIENT TEXTBOX
    t_fc_id = tk.Entry(master=lf_find_client, width=5)
    t_fc_name = tk.Entry(master=lf_find_client, width=10)
    t_fc_surname = tk.Entry(master=lf_find_client, width=10)

    t_fc_id.grid(row=0, column=1, sticky=tk.W)
    t_fc_name.grid(row=1, column=1, sticky=tk.W)
    t_fc_surname.grid(row=2, column=1, sticky=tk.W)

    # FIND CLIENT LIST BOX
    ages = []
    for i in range(1950, 2010):
        ages.append(i)
    ages_string = map(str, ages)
    str_of_ints = " ".join(ages_string)

    cb_fc_age = ttk.Combobox(master=lf_find_client, height=1, width=6, values=str_of_ints)
    cb_fc_age.grid(row=0, column=3, sticky=tk.W)

    chb_fc_active = tk.Checkbutton(master=lf_find_client, text="Aktivní", variable=active, onvalue=1, offvalue=0)
    chb_fc_active.grid(row=2, column=2, sticky=tk.W)

    rb_fc_man = tk.Radiobutton(master=lf_find_client, text="Muži", variable=gender, value=0)
    rb_fc_woman = tk.Radiobutton(master=lf_find_client, text="Ženy", variable=gender, value=1)

    rb_fc_man.grid(row=1, column=2, sticky=tk.N + tk.S + tk.W)
    rb_fc_woman.grid(row=1, column=3, columnspan=2, sticky=tk.N + tk.S + tk.W)

    b_fc_search = tk.Button(master=lf_find_client, text="Hledej", command=find_client)
    b_fc_search.grid(row=2, column=3)

    # FIND CLIENT
    # CLIENT CARD
    lf_client_info = tk.LabelFrame(master=f_first_page, text="Karta klienta")
    lf_client_info.rowconfigure(0, weight=1)
    lf_client_info.columnconfigure(0, weight=1)

    client_card_pages = ttk.Notebook(master=lf_client_info)

    # BASIC INFO
    f_client_info_basic = tk.Frame(padx=5, pady=5)
    for i in range(5):
        f_client_info_basic.rowconfigure(i, weight=1)
        f_client_info_basic.columnconfigure(i, weight=1)

    tk.Label(master=f_client_info_basic, text="Titul:").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_basic, text="Jméno:").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_basic, text="Příjmení:").grid(row=2, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_basic, text="Věk:").grid(row=3, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_basic, text="Zaměstnání:").grid(row=4, column=0, sticky=tk.N + tk.E + tk.S)

    t_ci_title = tk.Entry(master=f_client_info_basic, width=4)
    t_ci_title.grid(row=0, column=1, sticky=tk.W)
    t_ci_name = tk.Entry(master=f_client_info_basic, width=10)
    t_ci_name.grid(row=1, column=1, sticky=tk.W)
    t_ci_surname = tk.Entry(master=f_client_info_basic, width=10)
    t_ci_surname.grid(row=2, column=1, sticky=tk.W)
    t_ci_age = tk.Entry(master=f_client_info_basic, width=4)
    t_ci_age.grid(row=3, column=1, sticky=tk.W)
    t_ci_occupation = tk.Entry(master=f_client_info_basic, width=10)
    t_ci_occupation.grid(row=4, column=1, sticky=tk.W)

    f_client_info_basic.grid()
    # BASIC INFO

    # ADDRESS
    f_client_info_address = tk.Frame(padx=5, pady=5)
    for i in range(6):
        f_client_info_address.rowconfigure(i, weight=1)
        f_client_info_address.columnconfigure(i, weight=1)

    tk.Label(master=f_client_info_address, text="Telefon:").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_address, text="Email:").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_address, text="Ulice:").grid(row=2, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_address, text="Číslo popisné:").grid(row=3, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_address, text="Město:").grid(row=4, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_address, text="PSČ:").grid(row=5, column=0, sticky=tk.N + tk.E + tk.S)

    t_ci_phone = tk.Entry(master=f_client_info_address, width=10)
    t_ci_phone.grid(row=0, column=1, sticky=tk.W)
    t_ci_email = tk.Entry(master=f_client_info_address, width=20)
    t_ci_email.grid(row=1, column=1, sticky=tk.W)
    t_ci_street = tk.Entry(master=f_client_info_address, width=20)
    t_ci_street.grid(row=2, column=1, sticky=tk.W)
    t_ci_house_number = tk.Entry(master=f_client_info_address, width=8)
    t_ci_house_number.grid(row=3, column=1, sticky=tk.W)
    t_ci_town = tk.Entry(master=f_client_info_address, width=15)
    t_ci_town.grid(row=4, column=1, sticky=tk.W)
    t_ci_zip = tk.Entry(master=f_client_info_address, width=7)
    t_ci_zip.grid(row=5, column=1, sticky=tk.W)

    f_client_info_address.grid()
    # ADDRESS

    # PROGRESS
    f_client_info_progress = tk.Frame(padx=5, pady=5)
    for i in range(4):
        f_client_info_progress.rowconfigure(i, weight=1)
        f_client_info_progress.columnconfigure(i, weight=1)

    tk.Label(master=f_client_info_progress, text="Počáteční váha(kg):").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_progress, text="Počáteční % tuku:").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_progress, text="Počáteční obvod paže(cm):").grid(row=2, column=0,
                                                                                   sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_progress, text="Aktualní váha(kg):").grid(row=0, column=2, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_progress, text="Aktualní % tuku:").grid(row=1, column=2, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=f_client_info_progress, text="Aktualní obvod paže(cm):").grid(row=2, column=2,
                                                                                  sticky=tk.N + tk.E + tk.S)

    t_ci_s_weight = tk.Entry(master=f_client_info_progress, width=5)
    t_ci_s_weight.grid(row=0, column=1, sticky=tk.W)
    t_ci_s_fat = tk.Entry(master=f_client_info_progress, width=5)
    t_ci_s_fat.grid(row=1, column=1, sticky=tk.W)
    t_ci_s_arm = tk.Entry(master=f_client_info_progress, width=5)
    t_ci_s_arm.grid(row=2, column=1, sticky=tk.W)
    t_ci_a_weight = tk.Entry(master=f_client_info_progress, width=5)
    t_ci_a_weight.grid(row=0, column=3, sticky=tk.W)
    t_ci_a_fat = tk.Entry(master=f_client_info_progress, width=5)
    t_ci_a_fat.grid(row=1, column=3, sticky=tk.W)
    t_ci_a_arm = tk.Entry(master=f_client_info_progress, width=5)
    t_ci_a_arm.grid(row=2, column=3, sticky=tk.W)

    f_client_info_progress.grid()
    # PROGRESS

    client_card_pages.add(f_client_info_progress, text="Průběh spolupráce")
    client_card_pages.add(f_client_info_basic, text="Základní informace")
    client_card_pages.add(f_client_info_address, text="Adresa")
    client_card_pages.grid(sticky=tk.N + tk.E + tk.S + tk.W)

    # CLIENT CARD
    # GRID ITEMS
    lf_client_info.grid(row=0, column=1, columnspan=2, rowspan=2, sticky=tk.N + tk.E + tk.S + tk.W)
    lf_find_client.grid(row=0, column=0, rowspan=2, sticky=tk.N + tk.E + tk.S + tk.W)
    f_first_page.grid()
    # FIRST PAGE

    # SECOND PAGE
    f_second_page = tk.Frame()
    f_second_page.rowconfigure(0, weight=1)
    f_second_page.rowconfigure(1, weight=1)
    for i in range(3):
        f_second_page.columnconfigure(i, weight=1)

    # HISTORY
    lf_training_history = tk.LabelFrame(master=f_second_page, text="Historie tréninků")
    lf_training_history.rowconfigure(0, weight=1)
    lf_training_history.columnconfigure(0, weight=1)
    mlb_trainings = MultiListbox(lf_training_history, (('Název', 10), ('Délka', 4), ('Zaměření', 15)))
    mlb_trainings.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)

    lf_training_history.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    # HISTORY
    # EXERCISES
    lf_training_exercises = tk.LabelFrame(master=f_second_page, text="Cviky")
    lf_training_exercises.rowconfigure(0, weight=1)
    lf_training_exercises.columnconfigure(0, weight=1)
    mlb_exercises = MultiListbox(lf_training_exercises, (('Cvik', 10), ('Série', 4), ('Opakování', 4)))
    mlb_exercises.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    lf_training_exercises.grid(row=1, column=3, sticky=tk.N + tk.E + tk.S + tk.W)
    # EXERCISES

    # NEW TRAINING
    lf_training = tk.LabelFrame(master=f_second_page, text="Parametry tréninku")

    lf_training.rowconfigure(0, weight=1)
    lf_training.rowconfigure(1, weight=1)
    lf_training.rowconfigure(2, weight=1)
    for i in range(5):
        lf_training.columnconfigure(i, weight=1)

    tk.Label(master=lf_training, text="Název: ").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_training, text="Délka(min): ").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_training, text="Zaměření: ").grid(row=2, column=0, sticky=tk.N + tk.E + tk.S)

    t_t_name = tk.Entry(master=lf_training, width=10)
    t_t_length = tk.Entry(master=lf_training, width=5)
    t_t_focus = tk.Entry(master=lf_training, width=10)

    t_t_name.grid(row=0, column=1, sticky=tk.W)
    t_t_length.grid(row=1, column=1, sticky=tk.W)
    t_t_focus.grid(row=2, column=1, sticky=tk.W)

    # NEW EXERCISE
    lf_new_exercise = tk.LabelFrame(master=lf_training, text="Cviky")

    lf_new_exercise.columnconfigure(0, weight=1)
    lf_new_exercise.columnconfigure(1, weight=1)
    for i in range(5):
        lf_new_exercise.rowconfigure(i, weight=1)
    tk.Label(master=lf_new_exercise, text="Název: ").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_new_exercise, text="Opakování: ").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_new_exercise, text="Série: ").grid(row=2, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_new_exercise, text="Zátěž: ").grid(row=3, column=0, sticky=tk.N + tk.E + tk.S)

    t_t_exercise = tk.Entry(master=lf_new_exercise, width=10)
    t_t_reps = tk.Entry(master=lf_new_exercise, width=5)
    t_t_series = tk.Entry(master=lf_new_exercise, width=5)
    t_t_weight = tk.Entry(master=lf_new_exercise, width=5)

    t_t_exercise.grid(row=0, column=1, sticky=tk.W)
    t_t_reps.grid(row=1, column=1, sticky=tk.W)
    t_t_series.grid(row=2, column=1, sticky=tk.W)
    t_t_weight.grid(row=3, column=1, sticky=tk.W)

    b_add_ex = tk.Button(lf_new_exercise, text="Přidat")
    b_add_ex.grid(row=4, column=0, columnspan=2, sticky=tk.E + tk.W + tk.S)

    lf_new_exercise.grid(row=0, rowspan=3, column=2, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)

    # NEW EXERCISE

    lf_training.grid(row=1, column=0, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)
    # NEW TRAINING

    # PICKED TRAINING
    lf_picked_training = tk.LabelFrame(master=f_second_page, text="Parametry tréninku")

    lf_picked_training.rowconfigure(0, weight=1)
    lf_picked_training.rowconfigure(1, weight=1)
    lf_picked_training.rowconfigure(2, weight=1)
    for i in range(5):
        lf_picked_training.columnconfigure(i, weight=1)

    tk.Label(master=lf_picked_training, text="Název: ").grid(row=0, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_picked_training, text="Délka(min): ").grid(row=1, column=0, sticky=tk.N + tk.E + tk.S)
    tk.Label(master=lf_picked_training, text="Zaměření: ").grid(row=2, column=0, sticky=tk.N + tk.E + tk.S)

    t_t_name = tk.Entry(master=lf_picked_training, width=10)
    t_t_length = tk.Entry(master=lf_picked_training, width=5)
    t_t_focus = tk.Entry(master=lf_picked_training, width=10)

    t_t_name.grid(row=0, column=1, sticky=tk.W)
    t_t_length.grid(row=1, column=1, sticky=tk.W)
    t_t_focus.grid(row=2, column=1, sticky=tk.W)

    # NEW EXERCISE
    lf_exercises = tk.LabelFrame(master=lf_picked_training, text="Cviky")

    lf_exercises.columnconfigure(0, weight=1)
    lf_exercises.rowconfigure(0, weight=1)

    mlb_picked_exercises = MultiListbox(lf_exercises, (('Název', 10), ('Délka', 4), ('Zaměření', 15)))
    mlb_picked_exercises.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)

    lf_exercises.grid(row=0, rowspan=3, column=2, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)

    # NEW EXERCISE

    lf_picked_training.grid(row=0, column=1, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)
    # NEW TRAINING
    b_save_training = tk.Button(f_second_page, text="Uložit")
    b_save_training.grid(row=2, column=1, columnspan=2, sticky=tk.E + tk.W)

    f_second_page.grid()
    # SECOND PAGE

    main_pages.add(f_first_page, text="Informace o klientovi")
    main_pages.add(f_second_page, text="Přidat trénink")
    main_pages.grid(sticky=tk.N + tk.E + tk.S + tk.W)
    root.mainloop()
