from persons import Person


class Empoyer(Person):

    def __init__(self):
        Person.__init__(self, "ali", "karimi", 21, "iran")

    def setterEmpoyerID(self, id):
        self.empoyerid = id

    def getterEmpoyerID(self):
        return self.empoyerid


stu = Empoyer()
stu.setterEmpoyerID(1401312312)
print(str(stu.getterEmpoyerID()) + " " + stu.getterFirstnamePerson() + " " + stu.getterLastnamePerson())

