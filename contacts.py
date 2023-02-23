from faker import Faker

fake = Faker("pl_PL")


class Contacts:
    def __init__(self, first_name, surname, address, email):
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.email = email
        self._label_lenght = len(self.first_name) + len(self.surname) + 1

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"({self.first_name} {self.surname}, {self.email})"

    @property
    def label_lenght(self):
        return self._label_lenght


"""
    @label_lenght.setter
    def label_lenght(self, value):
        self._label_lenght = len(self.first_name) + len(self.surname) + 1
"""


class BaseContact(Contacts):
    def __init__(self, home_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.home_phone = home_phone

    def contact(self):
        if self.home_phone[0] == "+":
            print(
                "Wybieram numer %s i dzwonię do %s %s"
                % (self.home_phone, self.first_name, self.surname)
            )
        else:
            print(
                "Wybieram numer +48 %s i dzwonię do %s %s"
                % (self.home_phone, self.first_name, self.surname)
            )


class BusinessContact(Contacts):
    def __init__(self, job, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone = work_phone
        self.company = company
        self.job = job

    def contact(self):
        if self.work_phone[0] == "+":
            print(
                "Wybieram numer %s i dzwonię do %s %s"
                % (self.work_phone, self.first_name, self.surname)
            )
        else:
            print(
                "Wybieram numer +48 %s i dzwonię do %s %s"
                % (self.work_phone, self.first_name, self.surname)
            )


def create_contacts(kind, how_many):
    card_list = []
    if kind == BaseContact:
        for i in range(0, how_many):
            card = BaseContact(
                first_name=fake.first_name(),
                surname=fake.last_name(),
                address=fake.address(),
                email=fake.email(),
                home_phone=fake.phone_number(),
            )
            card_list.append(card)
        return card_list
    elif kind == BusinessContact:
        for i in range(0, how_many):
            card = BusinessContact(
                first_name=fake.first_name(),
                surname=fake.last_name(),
                address=fake.address(),
                email=fake.email(),
                work_phone=fake.phone_number(),
                company=fake.company(),
                job=fake.job(),
            )
            card_list.append(card)
        return card_list
    else:
        exit(1)


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

    karty = create_contacts(BaseContact, 5)
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

    print(karta.label_lenght)
    print(create_contacts(BaseContact, 5)[4].label_lenght)

    karty[3].contact()
    create_contacts(BusinessContact, 5)[2].contact()
    create_contacts(BaseContact, 5)[1].contact()
    print(type(create_contacts(BaseContact, 5)[1]))
    print(type(create_contacts(BaseContact, 5)))
    print(type(karta))
    print(create_contacts(BaseContact, 3))
    print(create_contacts(BusinessContact, 3))
    print(create_contacts(BaseContact, 3)[2].label_lenght)
    test_base = create_contacts(BaseContact, 3)[1]
    # test_base.label_lenght = 1
    print(test_base.label_lenght)
