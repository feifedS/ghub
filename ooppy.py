class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Животное издает звук.")

class Dog(Animal):
    def speak(self):
        print("Собака лает.")

my_dog = Dog("Бобик")
my_dog.speak()