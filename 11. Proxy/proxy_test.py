class Person:
  def __init__(self, age):
    self.age = age

  def drink(self):
    return 'drinking'

  def drive(self):
    return 'driving'

  def drink_and_drive(self):
    return 'driving while drunk'


class ResponsiblePerson:
  def __init__(self, person):
    self.person = person
    self.age = self.person.age
    
  def drink(self):
    if self.age>=18:
        return self.person.drink()
    else: 
        return "too young"
    

  def drive(self):
    if self.age>=16:
        return self.person.drive()
    else: 
        return "too young"

  def drink_and_drive(self):
    return "dead"