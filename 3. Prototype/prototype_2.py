from copy import deepcopy

class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'

class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:

    main_office_emp = Employee('',Address('123 East Drive', 0, 'London'))
    aux_office_emp = Employee('',Address('123B East Drive', 0, 'London'))

    @staticmethod
    def __new_emp(proto, name, suite):
        result = deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_emp(name, suite):
        return EmployeeFactory.__new_emp(
            EmployeeFactory.main_office_emp,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_emp(name, suite):
        return EmployeeFactory.__new_emp(
            EmployeeFactory.aux_office_emp,
            name,
            suite
        )


John = EmployeeFactory.new_main_office_emp('John', 500)
Jane = EmployeeFactory.new_aux_office_emp('Jane', 100)

print(John)
print(Jane)

