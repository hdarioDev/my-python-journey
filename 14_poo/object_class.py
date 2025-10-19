# ==============================
# OBJECT CLASS: BASIC EXAMPLE
# En Python, todas las clases heredan de 'object' por defecto
# object proporciona métodos especiales como:
# - __str__(): Representación en string (llamado implícitamente por print)
# - __eq__(): Comparación de igualdad
# - __init__(): Constructor
# - __class__: Referencia a la clase
# - __dict__: Diccionario de atributos
# ==============================

# Clase sin herencia explícita (hereda de object automáticamente)
# Nota: También se puede escribir explícitamente como: class Person(object):
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f'Hola, soy {self.name}')


# Crear instancia
person1 = Person('Juan')
person1.greet()  # Hola, soy Juan

# Ejemplo 1: Métodos heredados de object
print('\n*** Métodos heredados de object ***')
print(f'__class__: {person1.__class__}')  # <class '__main__.Person'>
print(f'__dict__: {person1.__dict__}')  # {'name': 'Juan'}
print(f'Person hereda de object? {issubclass(Person, object)}')  # True
print(f'person1 es instancia de object? {isinstance(person1, object)}')  # True


# Ejemplo 2: __str__ llamado implícitamente por print()
print('\n*** __str__ implícito vs explícito ***')
print(person1)  # Implícito: <__main__.Person object at 0x...>
print(person1.__str__())  # Explícito: <__main__.Person object at 0x...>


# Ejemplo 3: Sobrescribir __str__ y usar super()
class Employee(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job
    
    def __str__(self):
        # Usar super() para obtener el __str__ original de object
        original = super().__str__()
        return f'Employee: {self.name}, Job: {self.job} | Original: {original}'


emp = Employee('Ana', 'Developer')
print('\n*** Sobrescritura de __str__ ***')
print(emp)  # Employee: Ana, Job: Developer | Original: <__main__.Employee object at 0x...>
