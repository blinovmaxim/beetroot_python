class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        print("Woof Woof")

class Cat(Animal):
    def talk(self):
        print("Meow")


animal_Dog=Dog()
animal_Cat=Cat()

def Say(self):
    self.talk()
    

Say(animal_Cat)
Say(animal_Dog)


