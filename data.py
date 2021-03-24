from models.klient_address import ClientAddress
from models.klient import Client

address1 = ClientAddress(town="Ostrava", zip_code=12345, house_number=24, street="Modrá", email="mail@mail.com",
                         phone="123456789")
address2 = ClientAddress(town="Karviná", zip_code=67891, house_number=15, street="Zelená", email="test@mail.com",
                         phone="987654321")


client1 = Client(client_id=0, name="Jan", address=address1, active=True, s_weight=85, s_fat=19, gender=0,
                 surname="Železný", age=35, a_weight=90, a_fat=17)

client2 = Client(client_id=1, name="Simona", address=address2, active=False, s_weight=60, s_fat=16, gender=1,
                 surname="Cínová", age=29, a_weight=58, a_fat=15)

clients = [client1, client2]
