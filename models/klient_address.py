class ClientAddress:
    def __init__(self, town=None, phone=None, email=None, street=None, house_number=None, zip_code=None) -> None:
        super().__init__()
        self.phone = phone
        self.email = email
        self.street = street
        self.house_number = house_number
        self.town = town
        self.zip_code = zip_code
