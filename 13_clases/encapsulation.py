# Encapsulation example with private attributes
# ==============================
# ENCAPSULAMIENTO
# Ocultar los detalles de implementación y exponer solo lo necesario. _ para protegido y __ para privado
# python no es un lenguaje tan restrictivo como otros lenguajes por lo que se puede acceder a los atributos protegidos y privados
# ==============================

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

# Usando decoradores de python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


# Código de prueba fuera de la clase
person1 = Person("John", 30)
print(person1.name)
print(person1.age)
# Salida: John 30
person1.name = "Jane"
person1.age = 25
print(person1.name)
print(person1.age)
# Salida: Jane 25
