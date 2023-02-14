from faker import Faker

fake = Faker("pl_PL")


class Contacts:
    def __init__(self, first_name, surname, address, email):
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.email = email

        # veriables
        self.label_lenght = 0

    def __repr__(self):
        return f"Contacts{self}"

    def __str__(self):
        return f"({self.first_name} {self.surname}, {self.email})"

    @property
    def label_lenght(self):
        return self._label_lenght

    @label_lenght.setter
    def label_lenght(self, value):
        if value == 0:
            self._label_lenght = len(self.first_name) + len(self.surname) + 1


def create_contacts(how_many):
    card_list = []
    for i in range(0, how_many):
        card_list.append(card_list)
        card_list[i] = Contacts(
            first_name=fake.first_name(),
            surname=fake.last_name(),
            address=fake.address(),
            email=fake.email(),
        )
        # card_list[i].label_lenght = 0
    return card_list


if __name__ == "__main__":
    # Komendy testowe
    karta = Contacts(
        first_name="Witek",
        surname="Hungendorfer",
        address=fake.address(),
        email=fake.email(),
    )

    print(karta)
    print(karta.label_lenght)
    karty = create_contacts(5)
    for i in karty:
        print(i)

    print(karty)
    print("Długość nagłówka %s : %d" % (karty[1], karty[1].label_lenght))

    # SORTOWANIE
    by_first_name = sorted(karty, key=lambda card: card.first_name)
    by_surname = sorted(karty, key=lambda card: card.surname)
    by_email = sorted(karty, key=lambda card: card.email)
    print("Wizytówki posortowane po imieniu:", by_first_name)
    print("Wizytówki posortowane po nazwisku:", by_surname)
    print("Wizytówki posortowane po e-mail:", by_email)
