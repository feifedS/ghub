class MyClass:
    def __init__(self):
        self._private_variable = 10
        self.__protected_variable = 20

    def _private_method(self):
        print("Это приватный метод")

    def __protected_method(self):
        print("Это защищенный метод")

    def public_method(self):
        print("Это убличный метож")
        self._private_method()
        self.__protected_method()

my_object = MyClass()
my_object.public_method()

# Прямой доступ к приватным и защищенным переменным:
print(my_object._private_variable)
print(my_object._MyClass__protected_variable)
# Прямой доступ к приватным и защищенным методам:
my_object._private_method()
my_object._MyClass__protected_method()

