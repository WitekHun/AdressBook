from faker import Faker

fake = Faker("pl_PL")
from datetime import datetime


class Contacts:
    def __init__(self, first_name, surname, address, email):
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.email = email

        # veriables
        self.label_lenght = 0

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"({self.first_name} {self.surname}, {self.email})"

    @property
    def label_lenght(self):
        return self._label_lenght

    @label_lenght.setter
    def label_lenght(self, value):
        if True:
            self._label_lenght = len(self.first_name) + len(self.surname) + 1


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
            card_list.append(card_list)
            card_list[i] = BaseContact(
                first_name=fake.first_name(),
                surname=fake.last_name(),
                address=fake.address(),
                email=fake.email(),
                home_phone=fake.phone_number(),
            )
        return card_list
    elif kind == BusinessContact:
        for i in range(0, how_many):
            card_list.append(card_list)
            card_list[i] = BusinessContact(
                first_name=fake.first_name(),
                surname=fake.last_name(),
                address=fake.address(),
                email=fake.email(),
                work_phone=fake.phone_number(),
                company=fake.company(),
                job=fake.job(),
            )
            card_list[i].label_lenght = 0
        return card_list
    else:
        exit(1)


tstart = datetime.now()
print(tstart)

create_contacts(BaseContact, 10000)

tend = datetime.now()
print(tend)
print(tend - tstart)
