# ==============================
# POLYMORPHISM: BASIC EXAMPLE
# Ejemplo básico de polimorfismo en Python
# ==============================

# Clase base
class Animal:
    def make_sound(self):
        print('Algún sonido genérico')


# Clases derivadas con el mismo método pero diferente implementación
class Dog(Animal):
    def make_sound(self):
        print('Puedo ladrar')


class Cat(Animal):
    def make_sound(self):
        print('Puedo maullar')


# Ejemplo 1: Polimorfismo básico
print('*** Ejemplo Polimorfismo ***')

print('Clase Padre Animal: ')
animal1 = Animal()
animal1.make_sound()

print('\nClase Hija Dog: ')
dog1 = Dog()
dog1.make_sound()  # Polimorfismo

print('\nClase Hija Cat: ')
cat1 = Cat()
cat1.make_sound()  # Polimorfismo


# Ejemplo 2: Función polimórfica usando duck typing
def make_animal_sound(animal):  # duck typing
    animal.make_sound()


print('\n*** Ejemplo con Duck Typing ***')
make_animal_sound(animal1)
make_animal_sound(dog1)
make_animal_sound(cat1)
