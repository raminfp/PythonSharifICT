
class Person:

    def __init__(self, **kwargs):
        self.fname = kwargs["fname"]
        self.lname = kwargs["lname"]
        self.age = kwargs["age"]
        self.address = kwargs["adderss"]
        self.codeposti = ""


    # def setterPerson(self, fname, lname, age, address):
    #     self.fname = fname
    #     self.lname = lname
    #     self.age = age
    #     self.address = address
    #     self.codeposti = ""


    def getterFirstnamePerson(self):
        return self.fname

    def getterLastnamePerson(self):
        return self.lname

    def getterAgePerson(self):
        return self.age

    def getterAddressPerson(self):
        return self.address

    def gtterCodePosti(self):
        return self.codeposti
