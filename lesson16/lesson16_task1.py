class Person:

    def __init__(self,name,age,university):
        self.name=name
        self.age=age
        self.university=university
        
    def Hello(self):
        return print(f"Helllo, My name {self.name} and I am {self.age} years old")
class Student(Person):

    def grants(self):
        grants=1000
        return print (f"I am a student in {self.university} and have grant: ", grants)

class Teacher(Person):

    def salary(self):
        salary=15000
        print (f"I am a teacher in {self.university} and have salary: ",salary)

first_p=Student('Maxim',17,'Mechnikova')
first_p.Hello()
first_p.grants()

second_p=Teacher('Julia',35,'Mechnikova')
second_p.Hello()
second_p.salary()