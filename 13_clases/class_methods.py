# ==============================
# METHODS
# usar metodos para acceder a los atributos de clase con 3 formas :
# 1. Usando la instancia
# 2. Usando la static method
# 3. Usando class method
# ==============================

class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def get_counter_instance_method(self):
        print(f"This is an instance method, counter: {Person.counter}")

    @staticmethod
    def get_count_static_method():
        print(f"This is a static method, counter: {Person.counter}")


    @classmethod
    def get_count_class_method(cls):
        print(f"This is a class method, counter: {cls.counter}")

### Imprimir el contador ###
person1 = Person("John", 30)
person2 = Person("Jane", 25)
person1.get_counter_instance_method()
Person.get_count_static_method()
Person.get_count_class_method()
# Salida:
# This is an instance method, counter: 2
# This is a static method, counter: 2
# This is a class method, counter: 2
