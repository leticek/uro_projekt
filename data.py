from models.klient import Client
from models.klient_address import ClientAddress

address1 = ClientAddress(town="Ostrava", zip_code=12345, house_number=24, street="Modrá", email="mail@mail.com",
                         phone="123456789")
address2 = ClientAddress(town="Karviná", zip_code=67891, house_number=15, street="Zelená", email="test@mail.com",
                         phone="987654321")

client1 = Client(client_id=0, title="Bc.", occupation="technik", name="Jan", address=address1, active=True, s_weight=85,
                 s_fat=19, gender=0,
                 surname="Železný", age=35, a_weight=90, a_fat=17, s_arm=32, a_arm=34)

client2 = Client(client_id=1, title="Ing.",name="Simona", occupation="technik", address=address2, active=False, s_weight=60,
                 s_fat=16, gender=1,
                 surname="Cínová", age=29, a_weight=58, a_fat=15, s_arm=28, a_arm=29)
client3 = Client(client_id=2, title="Ing.",name="Petr", occupation="technik", address=address2, active=False, s_weight=60, s_fat=14,
                 gender=0,
                 surname="Cín", age=19, a_weight=65, a_fat=15, s_arm=28, a_arm=29)
client4 = Client(client_id=3, title="PhD.",name="Ludwig", occupation="technik", address=address1, active=True, s_weight=55, s_fat=17,
                 gender=0,
                 surname="Dub", age=22, a_weight=85, a_fat=15, s_arm=36, a_arm=38)

clients = [client1, client2, client3, client4]
