class Person:
    def __init__(self):
        
        self.street = None
        self.postcode = None
        self.city = None
        
        self.company_name = None
        self.position = None
        self.income= None

    def __str__(self) -> str:
        return f'Address: {self.street}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.income}'


class PersonBuilder:

    def __init__(self, person=Person()):
        self.person = person

    def build_P(self):
        return self.person        

    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return AddressJobBuilder(self.person)


class PersonJobBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earn(self, income):
        self.person.income = income
        return self

class AddressJobBuilder(PersonBuilder):

    def __init__(self, person):
        super().__init__(person)

    def at(self, street):
        self.person.street = street
        return self

    def at_p(self, postcode):
        self.person.postcode = postcode
        return self

    def in_c(self, city):
        self.person.city = city
        return self
    

 
pb = PersonBuilder()
P1 = pb\
    .lives\
        .at('Shivaji Nagar')\
            .in_c('Nagpur')\
                .at_p('737281')\
    .works\
        .at('Microsoft')\
            .as_a('Developer')\
                .earn('12 LPA')\
    .build_P()


print(P1)

