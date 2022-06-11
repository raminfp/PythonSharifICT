from persons import Person


class Student(Person):

    def __init__(self):
        # Person.__init__(self, fname="ramin", lname="fp", age=20, adderss="US")
        super().__init__(fname="ramin", lname="fp", age=20, adderss="US")

    def setterStudentID(self, id):
        self.studentid = id

    def getterStudentID(self):
        return self.studentid

    def register(self):
        # insert to database
        pass


stu = Student()
# form (/register - /signup ) --- form desktop
# stu.setterPerson("ramin", "fp", 12, "tehran")
stu.setterStudentID(1401312312)
print(str(stu.getterStudentID()) + " " + stu.getterFirstnamePerson() + " " + stu.getterLastnamePerson())

stu.register()
