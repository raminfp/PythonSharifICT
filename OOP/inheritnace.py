
class Animal:

    def __init__(self):
        print("Animal created")

    def whoAmi(self):
        print("I'm Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        # Animal.whoAmi(self)
        print("Dog created")

    def whoAmi(self):
        print("Dog")

    def DogEat(self):
        print("Dog Eating")


d = Dog()
Animal.whoAmi(d)
d.eat()
d.whoAmi()