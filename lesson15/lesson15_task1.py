from unicodedata import name


class Person:
    def __init__(self):
        self.firstname=0
        self.lastname=0
        self.age=0
    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'am {self.age} years old")

first_person=Person()
first_person.firstname = 'Carl'
first_person.lastname = 'Jonson'
first_person.age = 26
first_person.talk()