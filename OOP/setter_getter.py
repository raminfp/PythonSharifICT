# setter / getter

class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def setterName(self):
        self.fullname = f'{self.fname} {self.lname}'

    def getterName(self):
        return self.fullname


person = Person("ramin", "fp")
person.setterName()
print(person.getterName())
