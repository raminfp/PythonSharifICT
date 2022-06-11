
class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} say Woofff'


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} say maooo'

dog = Dog("Joli")
cat = Cat("Gogoli")
#
# print(dog.speak())
# print(cat.speak())

for item in [dog, cat]:
    print(item.speak())

