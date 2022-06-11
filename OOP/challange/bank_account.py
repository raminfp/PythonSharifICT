
class Account:

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    def __str__(self):
        return f'Account owner : {self.owner}\n Account amount : {self.amount}'

    def decmoney(self, code):
        self.amount -= code
        print("code takhfif is done")

    def showamount(self):
        return self.amount

acc1 = Account("ramin", 1000)
print(acc1)
acc1.decmoney(20)
print(acc1.showamount())

