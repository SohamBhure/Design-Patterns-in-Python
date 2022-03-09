from copy import copy, deepcopy

class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


address = Address("123 London Road", "London", "England")
John = Person("John", address)

Jane = Person("Jane", address)
print(John)
print(Jane)

Jane.address.street_address = '123c'
print(John)
print(Jane)

Jesse = deepcopy(John)
Jesse.name = 'Jesse'
Jesse.address.street_address = '123B'
print(John)
print(Jesse)
