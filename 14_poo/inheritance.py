# ==============================
# INHERITANCE: BASIC EXAMPLE
# Herencia permite que una clase hija herede atributos y métodos de una clase padre
# super() se usa para acceder a métodos y atributos de la clase padre
# ==============================

# Ejemplo 1: Herencia simple sin constructor
class Vehicle:
    def start(self):
        print('El vehículo está encendido')
    
    def stop(self):
        print('El vehículo está apagado')


class Car(Vehicle):
    def honk(self):
        print('Beep beep!')


my_car = Car()
my_car.start()  # El vehículo está encendido
my_car.stop()   # El vehículo está apagado
my_car.honk()   # Beep beep!


# Ejemplo 2: Herencia con super() para atributos
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def __str__(self):
        return f'Person: name={self.name}, last_name={self.last_name}'


class Employee(Person):
    def __init__(self, name, last_name, salary):
        # Usar super() para inicializar atributos de la clase padre
        super().__init__(name, last_name)
        self.salary = salary
    
    def __str__(self):
        # Usar super() para obtener el __str__ del padre
        return f'{super().__str__()} | Employee: salary={self.salary}'


print('\n*** Ejemplo con super() ***')
emp = Employee('Juan', 'Pérez', 5000)
print(emp)  # Person: name=Juan, last_name=Pérez | Employee: salary=5000
