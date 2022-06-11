# Objects
# class keyword
# class attributes
# methods in class
# about inheritance
# polymorphism
# special methods

lst = [1, 2, 3, 2]
print(type(lst))
print(type(()))
print(type({}))
print(type(1))


class FirstClass:

    # Class Object Attributes
    dbname = "connection to database"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def show(self):
    #     # object connect to database
    #     # object insert/delete/update/selecone/selectall
    #     print(self.)

    def suming(self):
        return self.a + self.b

    def sub(self):
        return self.b - self.a


x = FirstClass(10, 30)
print(x.suming())
print(x.sub())
# x.show()

