class Dog:
    def __init__(self):
        self.age_factor=7
        self.age_dog=0
    def human_age(self):
        human_equal=self.age_dog*self.age_factor
        return human_equal


human_age_calc=Dog()
human_age_calc.age_dog=7
print("Dog age is", human_age_calc.age_dog)
print("Dog's age in human equivalent: ",human_age_calc.human_age())
