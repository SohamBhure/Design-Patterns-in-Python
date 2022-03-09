class Person:

    def __init__(self) -> None:

        self.name = None
        self.position = None
        self.DOB = None

    def __str__(self) -> str:
        return f'{self.name} - {self.DOB} - {self.position}'
    
    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder():

    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, DOB):
        self.person.DOB = DOB
        return self


P1 = PersonBirthDateBuilder()
me = P1\
        .called('Dmitri')\
        .works_as_a('quant')\
        .born('1/1/1980')\
        .build()  # this does NOT work in C#/C++/Java/...
print(me)