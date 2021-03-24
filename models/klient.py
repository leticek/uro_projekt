class Client:

    def __init__(self, client_id=None, name=None, surname=None, age=None, gender=None, active=None, s_weight=None,
                 s_fat=None, address=None, a_fat=None, a_weight=None, a_arm=None, s_arm=None) -> None:
        super().__init__()

        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.active = active
        self.s_weight = s_weight
        self.s_fat = s_fat
        self.a_weight = a_weight
        self.a_fat = a_fat
        self.s_arm = s_arm
        self.a_arm = a_arm
        self.address = address
