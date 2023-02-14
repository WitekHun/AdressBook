from faker import Faker
fake = Faker('pl_PL')


class Contacts:
    def __init__(self, first_name, surname, address, email):
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.email = email

        # veriables
        self._label_lenght = 0

    def __repr__(self):
        return f'{self}'

    def __str__(self):
        return f"({self.first_name} {self.surname}, {self.email})"

   
