import tkinter as tk
from tkinter import ttk

from data import clients, trainings
from models.exercise import Exercise
from models.klient import Client
from models.training_plan import TrainingPlan
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
    lf_training_history = tk.LabelFrame(master=f_second_page, text="Seznam tréninků")
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
    mlb_exercises = MultiListbox(lf_training_exercises, (('Cvik', 10), ('Série', 4), ('Opakování', 4), ('Váha', 4)))
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

    added_exercises = []


    def add_exercise(exercise, reps, series, weight):
        t_t_exercise.delete(0, 'end')
        t_t_weight.delete(0, 'end')
        t_t_reps.delete(0, 'end')
        t_t_series.delete(0, 'end')
        added_exercises.append(Exercise(exercise=exercise, weight=weight, series=series, reps=reps))
        mlb_exercises.insert(tk.END, (exercise, series, reps, weight))


    b_add_ex = tk.Button(lf_new_exercise, text="Přidat",
                         command=lambda: add_exercise(t_t_exercise.get(), t_t_reps.get(), t_t_series.get(),
                                                      t_t_weight.get()))
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

    t_pt_name = tk.Entry(master=lf_picked_training, width=10)
    t_pt_length = tk.Entry(master=lf_picked_training, width=5)
    t_pt_focus = tk.Entry(master=lf_picked_training, width=10)

    t_pt_name.grid(row=0, column=1, sticky=tk.W)
    t_pt_length.grid(row=1, column=1, sticky=tk.W)
    t_pt_focus.grid(row=2, column=1, sticky=tk.W)

    #  EXERCISES
    lf_exercises = tk.LabelFrame(master=lf_picked_training, text="Cviky")

    lf_exercises.columnconfigure(0, weight=1)
    lf_exercises.rowconfigure(0, weight=1)


    def choose_training(row):
        t_pt_name.delete(0, tk.END)
        t_pt_length.delete(0, tk.END)
        t_pt_focus.delete(0, tk.END)
        mlb_picked_exercises.delete(0, 150)
        t = trainings[row]
        for ex in t.exercises:
            mlb_picked_exercises.insert(tk.END, (ex.exercise, ex.series, ex.reps, ex.weight))
        t_pt_name.insert(0, t.name)
        t_pt_length.insert(0, t.length)
        t_pt_focus.insert(0, t.focus)


    mlb_picked_exercises = MultiListbox(lf_exercises, (('Cvik', 10), ('Série', 4), ('Opakování', 4), ('Váha', 4)))
    mlb_picked_exercises.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    mlb_trainings.subscribe(lambda row: choose_training(row))

    lf_exercises.grid(row=0, rowspan=3, column=2, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)
    #  EXERCISES

    lf_picked_training.grid(row=0, column=1, columnspan=3, sticky=tk.N + tk.E + tk.S + tk.W)


    # PICKED TRAINING

    def add_training(name, length, focus):
        t = TrainingPlan(client=clients[current_client], name=name, length=length, focus=focus,
                         exercises=added_exercises)
        mlb_exercises.delete(0, 150)
        t_t_name.delete(0, tk.END)
        t_t_length.delete(0, tk.END)
        t_t_focus.delete(0, tk.END)
        trainings.append(t)
        mlb_trainings.insert(tk.END, (t.name, t.length, t.focus))


    b_save_training = tk.Button(f_second_page, text="Uložit",
                                command=lambda: add_training(t_t_name.get(), t_t_length.get(), t_t_focus.get()))
    b_save_training.grid(row=2, column=1, columnspan=2, sticky=tk.E + tk.W)

    f_second_page.grid()
    # SECOND PAGE

    # THIRD PAGE
    f_third_page = tk.Frame()
    f_third_page.rowconfigure(0, weight=1)
    f_third_page.rowconfigure(1, weight=1)
    for i in range(5):
        f_third_page.columnconfigure(i, weight=1)

    # MEAL PLANS
    lf_meal_plans = tk.LabelFrame(master=f_third_page, text="Plány")
    lf_meal_plans.rowconfigure(0, weight=1)
    lf_meal_plans.columnconfigure(0, weight=1)
    mlb_meal_plans = MultiListbox(lf_meal_plans, (("Název", 10), ("Kategorie", 10)))
    mlb_meal_plans.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    lf_meal_plans.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    # MEAL PLANS

    # PLAN SETTINGS
    lf_plan_settings = tk.LabelFrame(master=f_third_page, text="Parametry plánu")
    lf_plan_settings.columnconfigure(0, weight=1)
    lf_plan_settings.columnconfigure(1, weight=1)
    for i in range(4):
        lf_plan_settings.rowconfigure(i, weight=1)

    tk.Label(master=lf_plan_settings, text="Název: ").grid(row=0, column=0, sticky=tk.E)

    t_ps_name = tk.Entry(master=lf_plan_settings, width=20)
    t_ps_name.grid(row=0, column=1, sticky=tk.W)

    cb_vegan = tk.StringVar()
    cb_keto = tk.StringVar()
    cb_diet = tk.StringVar()
    cb_veget = tk.StringVar()
    cb_carb_waves = tk.StringVar()
    cb_bulk = tk.StringVar()

    cb_ps_vegan = tk.Checkbutton(master=lf_plan_settings, text="Vegan", variable=cb_vegan, onvalue="Vegan", offvalue="")
    cb_ps_keto = tk.Checkbutton(master=lf_plan_settings, text="Keto-dieta", variable=cb_keto, onvalue="Keto-diet",
                                offvalue="")
    cb_ps_diet = tk.Checkbutton(master=lf_plan_settings, text="Dieta", variable=cb_diet, onvalue="Dieta", offvalue="")
    cb_ps_veget = tk.Checkbutton(master=lf_plan_settings, text="Vegetarián", variable=cb_veget, onvalue="Vegetarian",
                                 offvalue="")
    cb_ps_carb_waves = tk.Checkbutton(master=lf_plan_settings, text="Sacharidové vlny", variable=cb_carb_waves,
                                      onvalue="Sacharidové vlny", offvalue="")
    cb_ps_bulk = tk.Checkbutton(master=lf_plan_settings, text="Objem", variable=cb_bulk, onvalue="Objem", offvalue="")

    cb_ps_vegan.grid(row=1, column=0, sticky=tk.S + tk.W + tk.N)
    cb_ps_keto.grid(row=2, column=0, sticky=tk.S + tk.W + tk.N)
    cb_ps_diet.grid(row=3, column=0, sticky=tk.S + tk.W + tk.N)
    cb_ps_veget.grid(row=1, column=1, sticky=tk.S + tk.W + tk.N)
    cb_ps_carb_waves.grid(row=2, column=1, sticky=tk.S + tk.W + tk.N)
    cb_ps_bulk.grid(row=3, column=1, sticky=tk.S + tk.W + tk.N)

    lf_plan_settings.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S + tk.W)


    def save_plan():
        print(cb_vegan.get())


    b_save_plan = tk.Button(master=lf_plan_settings, text="Uložit", command=save_plan)
    b_save_plan.grid(row=4, column=0, columnspan=2, sticky=tk.N + tk.E + tk.S + tk.W)
    # PLAN SETTINGS

    # PLAN
    lf_meal_plan = tk.LabelFrame(master=f_third_page, text="Parametry plánu")
    lf_meal_plan.rowconfigure(0, weight=1)
    lf_meal_plan.rowconfigure(1, weight=1)
    for i in range(3):
        lf_meal_plan.columnconfigure(i, weight=1)
    # BREAKFAST
    lf_np_breakfast = tk.LabelFrame(master=lf_meal_plan, text="Snídaně")

    for i in range(4):
        lf_np_breakfast.columnconfigure(i, weight=1)
    for i in range(5):
        lf_np_breakfast.rowconfigure(i, weight=1)

    t_br_food = tk.Text(master=lf_np_breakfast, width=10, height=6)
    t_br_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_np_breakfast, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_breakfast, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_breakfast, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_breakfast, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_breakfast, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_np_br_cal = tk.Entry(master=lf_np_breakfast, width=10)
    t_np_br_pro = tk.Entry(master=lf_np_breakfast, width=10)
    t_np_br_car = tk.Entry(master=lf_np_breakfast, width=10)
    t_np_br_fat = tk.Entry(master=lf_np_breakfast, width=10)
    t_np_br_fib = tk.Entry(master=lf_np_breakfast, width=10)

    t_np_br_cal.grid(row=0, column=3, sticky=tk.W)
    t_np_br_pro.grid(row=1, column=3, sticky=tk.W)
    t_np_br_car.grid(row=2, column=3, sticky=tk.W)
    t_np_br_fat.grid(row=3, column=3, sticky=tk.W)
    t_np_br_fib.grid(row=4, column=3, sticky=tk.W)

    lf_np_breakfast.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    # BREAKFAST

    # SNACK 1
    lf_np_snack1 = tk.LabelFrame(master=lf_meal_plan, text="Svačina 1")

    for i in range(4):
        lf_np_snack1.columnconfigure(i, weight=1)
    for i in range(5):
        lf_np_snack1.rowconfigure(i, weight=1)

    t_s1_food = tk.Text(master=lf_np_snack1, width=10, height=6)
    t_s1_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_np_snack1, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack1, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack1, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack1, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack1, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_np_s1_cal = tk.Entry(master=lf_np_snack1, width=10)
    t_np_s1_pro = tk.Entry(master=lf_np_snack1, width=10)
    t_np_s1_car = tk.Entry(master=lf_np_snack1, width=10)
    t_np_s1_fat = tk.Entry(master=lf_np_snack1, width=10)
    t_np_s1_fib = tk.Entry(master=lf_np_snack1, width=10)

    t_np_s1_cal.grid(row=0, column=3, sticky=tk.W)
    t_np_s1_pro.grid(row=1, column=3, sticky=tk.W)
    t_np_s1_car.grid(row=2, column=3, sticky=tk.W)
    t_np_s1_fat.grid(row=3, column=3, sticky=tk.W)
    t_np_s1_fib.grid(row=4, column=3, sticky=tk.W)

    lf_np_snack1.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    # SNACK 1

    # LUNCH
    lf_np_lunch = tk.LabelFrame(master=lf_meal_plan, text="Oběd")

    for i in range(4):
        lf_np_lunch.columnconfigure(i, weight=1)
    for i in range(5):
        lf_np_lunch.rowconfigure(i, weight=1)

    t_lc_food = tk.Text(master=lf_np_lunch, width=10, height=6)
    t_lc_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_np_lunch, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_lunch, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_lunch, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_lunch, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_lunch, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_np_lc_cal = tk.Entry(master=lf_np_lunch, width=10)
    t_np_lc_pro = tk.Entry(master=lf_np_lunch, width=10)
    t_np_lc_car = tk.Entry(master=lf_np_lunch, width=10)
    t_np_lc_fat = tk.Entry(master=lf_np_lunch, width=10)
    t_np_lc_fib = tk.Entry(master=lf_np_lunch, width=10)

    t_np_lc_cal.grid(row=0, column=3, sticky=tk.W)
    t_np_lc_pro.grid(row=1, column=3, sticky=tk.W)
    t_np_lc_car.grid(row=2, column=3, sticky=tk.W)
    t_np_lc_fat.grid(row=3, column=3, sticky=tk.W)
    t_np_lc_fib.grid(row=4, column=3, sticky=tk.W)

    lf_np_lunch.grid(row=0, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
    # LUNCH

    # DINNER
    lf_np_dinner = tk.LabelFrame(master=lf_meal_plan, text="Večeře")

    for i in range(4):
        lf_np_dinner.columnconfigure(i, weight=1)
    for i in range(5):
        lf_np_dinner.rowconfigure(i, weight=1)

    t_d_food = tk.Text(master=lf_np_dinner, width=10, height=6)
    t_d_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_np_dinner, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_np_d_cal = tk.Entry(master=lf_np_dinner, width=10)
    t_np_d_pro = tk.Entry(master=lf_np_dinner, width=10)
    t_np_d_car = tk.Entry(master=lf_np_dinner, width=10)
    t_np_d_fat = tk.Entry(master=lf_np_dinner, width=10)
    t_np_d_fib = tk.Entry(master=lf_np_dinner, width=10)

    t_np_d_cal.grid(row=0, column=3, sticky=tk.W)
    t_np_d_pro.grid(row=1, column=3, sticky=tk.W)
    t_np_d_car.grid(row=2, column=3, sticky=tk.W)
    t_np_d_fat.grid(row=3, column=3, sticky=tk.W)
    t_np_d_fib.grid(row=4, column=3, sticky=tk.W)

    lf_np_dinner.grid(row=0, column=2, sticky=tk.N + tk.E + tk.S + tk.W)
    # DINNER

    # SNACK 1
    lf_np_snack2 = tk.LabelFrame(master=lf_meal_plan, text="Svačina 2")

    for i in range(4):
        lf_np_snack2.columnconfigure(i, weight=1)
    for i in range(5):
        lf_np_snack2.rowconfigure(i, weight=1)

    t_s1_food = tk.Text(master=lf_np_snack2, width=10, height=6)
    t_s1_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_np_snack2, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack2, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack2, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack2, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_snack2, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_np_s2_cal = tk.Entry(master=lf_np_snack2, width=10)
    t_np_s2_pro = tk.Entry(master=lf_np_snack2, width=10)
    t_np_s2_car = tk.Entry(master=lf_np_snack2, width=10)
    t_np_s2_fat = tk.Entry(master=lf_np_snack2, width=10)
    t_np_s2_fib = tk.Entry(master=lf_np_snack2, width=10)

    t_np_s2_cal.grid(row=0, column=3, sticky=tk.W)
    t_np_s2_pro.grid(row=1, column=3, sticky=tk.W)
    t_np_s2_car.grid(row=2, column=3, sticky=tk.W)
    t_np_s2_fat.grid(row=3, column=3, sticky=tk.W)
    t_np_s2_fib.grid(row=4, column=3, sticky=tk.W)

    lf_np_snack2.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
    # SNACK 1

    # BEFORE SLEEP
    lf_np_dinner2 = tk.LabelFrame(master=lf_meal_plan, text="Před spaním")

    for i in range(4):
        lf_np_dinner2.columnconfigure(i, weight=1)
    for i in range(5):
        lf_np_dinner2.rowconfigure(i, weight=1)

    t_d2_food = tk.Text(master=lf_np_dinner2, width=10, height=6)
    t_d2_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_np_dinner2, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner2, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner2, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner2, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_np_dinner2, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_np_d2_cal = tk.Entry(master=lf_np_dinner2, width=10)
    t_np_d2_pro = tk.Entry(master=lf_np_dinner2, width=10)
    t_np_d2_car = tk.Entry(master=lf_np_dinner2, width=10)
    t_np_d2_fat = tk.Entry(master=lf_np_dinner2, width=10)
    t_np_d2_fib = tk.Entry(master=lf_np_dinner2, width=10)

    t_np_d2_cal.grid(row=0, column=3, sticky=tk.W)
    t_np_d2_pro.grid(row=1, column=3, sticky=tk.W)
    t_np_d2_car.grid(row=2, column=3, sticky=tk.W)
    t_np_d2_fat.grid(row=3, column=3, sticky=tk.W)
    t_np_d2_fib.grid(row=4, column=3, sticky=tk.W)

    lf_np_dinner2.grid(row=1, column=2, sticky=tk.N + tk.E + tk.S + tk.W)
    # BEFORE SLEEP

    lf_meal_plan.grid(row=1, column=1, columnspan=4, sticky=tk.N + tk.E + tk.S + tk.W)
    # PLAN

    # PICKED PLAN
    lf_meal_plan_picked = tk.LabelFrame(master=f_third_page, text="Vybraný plán")
    lf_meal_plan_picked.rowconfigure(0, weight=1)
    lf_meal_plan_picked.rowconfigure(1, weight=1)
    for i in range(3):
        lf_meal_plan_picked.columnconfigure(i, weight=1)
    # BREAKFAST
    lf_pp_breakfast = tk.LabelFrame(master=lf_meal_plan_picked, text="Snídaně")

    for i in range(4):
        lf_pp_breakfast.columnconfigure(i, weight=1)
    for i in range(5):
        lf_pp_breakfast.rowconfigure(i, weight=1)

    t_br_food = tk.Text(master=lf_pp_breakfast, width=10, height=6)
    t_br_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_pp_breakfast, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_breakfast, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_breakfast, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_breakfast, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_breakfast, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_pp_br_cal = tk.Entry(master=lf_pp_breakfast, width=10)
    t_pp_br_pro = tk.Entry(master=lf_pp_breakfast, width=10)
    t_pp_br_car = tk.Entry(master=lf_pp_breakfast, width=10)
    t_pp_br_fat = tk.Entry(master=lf_pp_breakfast, width=10)
    t_pp_br_fib = tk.Entry(master=lf_pp_breakfast, width=10)

    t_pp_br_cal.grid(row=0, column=3, sticky=tk.W)
    t_pp_br_pro.grid(row=1, column=3, sticky=tk.W)
    t_pp_br_car.grid(row=2, column=3, sticky=tk.W)
    t_pp_br_fat.grid(row=3, column=3, sticky=tk.W)
    t_pp_br_fib.grid(row=4, column=3, sticky=tk.W)

    lf_pp_breakfast.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    # BREAKFAST

    # SNACK 1
    lf_pp_snack1 = tk.LabelFrame(master=lf_meal_plan_picked, text="Svačina 1")

    for i in range(4):
        lf_pp_snack1.columnconfigure(i, weight=1)
    for i in range(5):
        lf_pp_snack1.rowconfigure(i, weight=1)

    t_s1_food = tk.Text(master=lf_pp_snack1, width=10, height=6)
    t_s1_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_pp_snack1, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack1, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack1, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack1, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack1, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_pp_s1_cal = tk.Entry(master=lf_pp_snack1, width=10)
    t_pp_s1_pro = tk.Entry(master=lf_pp_snack1, width=10)
    t_pp_s1_car = tk.Entry(master=lf_pp_snack1, width=10)
    t_pp_s1_fat = tk.Entry(master=lf_pp_snack1, width=10)
    t_pp_s1_fib = tk.Entry(master=lf_pp_snack1, width=10)

    t_pp_s1_cal.grid(row=0, column=3, sticky=tk.W)
    t_pp_s1_pro.grid(row=1, column=3, sticky=tk.W)
    t_pp_s1_car.grid(row=2, column=3, sticky=tk.W)
    t_pp_s1_fat.grid(row=3, column=3, sticky=tk.W)
    t_pp_s1_fib.grid(row=4, column=3, sticky=tk.W)

    lf_pp_snack1.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
    # SNACK 1

    # LUNCH
    lf_pp_lunch = tk.LabelFrame(master=lf_meal_plan_picked, text="Oběd")

    for i in range(4):
        lf_pp_lunch.columnconfigure(i, weight=1)
    for i in range(5):
        lf_pp_lunch.rowconfigure(i, weight=1)

    t_lc_food = tk.Text(master=lf_pp_lunch, width=10, height=6)
    t_lc_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_pp_lunch, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_lunch, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_lunch, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_lunch, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_lunch, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_pp_lc_cal = tk.Entry(master=lf_pp_lunch, width=10)
    t_pp_lc_pro = tk.Entry(master=lf_pp_lunch, width=10)
    t_pp_lc_car = tk.Entry(master=lf_pp_lunch, width=10)
    t_pp_lc_fat = tk.Entry(master=lf_pp_lunch, width=10)
    t_pp_lc_fib = tk.Entry(master=lf_pp_lunch, width=10)

    t_pp_lc_cal.grid(row=0, column=3, sticky=tk.W)
    t_pp_lc_pro.grid(row=1, column=3, sticky=tk.W)
    t_pp_lc_car.grid(row=2, column=3, sticky=tk.W)
    t_pp_lc_fat.grid(row=3, column=3, sticky=tk.W)
    t_pp_lc_fib.grid(row=4, column=3, sticky=tk.W)

    lf_pp_lunch.grid(row=0, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
    # LUNCH

    # DINNER
    lf_pp_dinner = tk.LabelFrame(master=lf_meal_plan_picked, text="Večeře")

    for i in range(4):
        lf_pp_dinner.columnconfigure(i, weight=1)
    for i in range(5):
        lf_pp_dinner.rowconfigure(i, weight=1)

    t_d_food = tk.Text(master=lf_pp_dinner, width=10, height=6)
    t_d_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_pp_dinner, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_pp_d_cal = tk.Entry(master=lf_pp_dinner, width=10)
    t_pp_d_pro = tk.Entry(master=lf_pp_dinner, width=10)
    t_pp_d_car = tk.Entry(master=lf_pp_dinner, width=10)
    t_pp_d_fat = tk.Entry(master=lf_pp_dinner, width=10)
    t_pp_d_fib = tk.Entry(master=lf_pp_dinner, width=10)

    t_pp_d_cal.grid(row=0, column=3, sticky=tk.W)
    t_pp_d_pro.grid(row=1, column=3, sticky=tk.W)
    t_pp_d_car.grid(row=2, column=3, sticky=tk.W)
    t_pp_d_fat.grid(row=3, column=3, sticky=tk.W)
    t_pp_d_fib.grid(row=4, column=3, sticky=tk.W)

    lf_pp_dinner.grid(row=0, column=2, sticky=tk.N + tk.E + tk.S + tk.W)
    # DINNER

    # SNACK 1
    lf_pp_snack2 = tk.LabelFrame(master=lf_meal_plan_picked, text="Svačina 2")

    for i in range(4):
        lf_pp_snack2.columnconfigure(i, weight=1)
    for i in range(5):
        lf_pp_snack2.rowconfigure(i, weight=1)

    t_s1_food = tk.Text(master=lf_pp_snack2, width=10, height=6)
    t_s1_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_pp_snack2, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack2, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack2, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack2, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_snack2, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_pp_s2_cal = tk.Entry(master=lf_pp_snack2, width=10)
    t_pp_s2_pro = tk.Entry(master=lf_pp_snack2, width=10)
    t_pp_s2_car = tk.Entry(master=lf_pp_snack2, width=10)
    t_pp_s2_fat = tk.Entry(master=lf_pp_snack2, width=10)
    t_pp_s2_fib = tk.Entry(master=lf_pp_snack2, width=10)

    t_pp_s2_cal.grid(row=0, column=3, sticky=tk.W)
    t_pp_s2_pro.grid(row=1, column=3, sticky=tk.W)
    t_pp_s2_car.grid(row=2, column=3, sticky=tk.W)
    t_pp_s2_fat.grid(row=3, column=3, sticky=tk.W)
    t_pp_s2_fib.grid(row=4, column=3, sticky=tk.W)

    lf_pp_snack2.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
    # SNACK 1

    # BEFORE SLEEP
    lf_pp_dinner2 = tk.LabelFrame(master=lf_meal_plan_picked, text="Před spaním")

    for i in range(4):
        lf_pp_dinner2.columnconfigure(i, weight=1)
    for i in range(5):
        lf_pp_dinner2.rowconfigure(i, weight=1)

    t_d2_food = tk.Text(master=lf_pp_dinner2, width=10, height=6)
    t_d2_food.grid(row=0, column=0, columnspan=2, rowspan=5, sticky=tk.N + tk.E + tk.S + tk.W)

    tk.Label(master=lf_pp_dinner2, text="Kalorie: ").grid(row=0, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner2, text="Bílkoviny: ").grid(row=1, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner2, text="Sacharidy: ").grid(row=2, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner2, text="Tuky: ").grid(row=3, column=2, sticky=tk.W + tk.S + tk.N)
    tk.Label(master=lf_pp_dinner2, text="Vláknina: ").grid(row=4, column=2, sticky=tk.W + tk.S + tk.N)

    t_pp_d2_cal = tk.Entry(master=lf_pp_dinner2, width=10)
    t_pp_d2_pro = tk.Entry(master=lf_pp_dinner2, width=10)
    t_pp_d2_car = tk.Entry(master=lf_pp_dinner2, width=10)
    t_pp_d2_fat = tk.Entry(master=lf_pp_dinner2, width=10)
    t_pp_d2_fib = tk.Entry(master=lf_pp_dinner2, width=10)

    t_pp_d2_cal.grid(row=0, column=3, sticky=tk.W)
    t_pp_d2_pro.grid(row=1, column=3, sticky=tk.W)
    t_pp_d2_car.grid(row=2, column=3, sticky=tk.W)
    t_pp_d2_fat.grid(row=3, column=3, sticky=tk.W)
    t_pp_d2_fib.grid(row=4, column=3, sticky=tk.W)

    lf_pp_dinner2.grid(row=1, column=2, sticky=tk.N + tk.E + tk.S + tk.W)
    # BEFORE SLEEP

    lf_meal_plan_picked.grid(row=0, column=1, columnspan=4, sticky=tk.N + tk.E + tk.S + tk.W)
    # PICKED PLAN

    f_third_page.grid()
    # THIRD PAGE

    main_pages.add(f_first_page, text="Informace o klientovi")
    main_pages.add(f_second_page, text="Přidat trénink")
    main_pages.add(f_third_page, text="Jídelní plány")
    main_pages.grid(sticky=tk.N + tk.E + tk.S + tk.W)
    root.mainloop()
