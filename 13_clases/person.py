# Definicion de una clase
class Person:
    # Python no tiene sobre carga de constructores
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"ID objeto: {id(self)}")
        print(f"Dir memoria: {hex(id(self))}")

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Crear una instancia de la clase
person = Person("John", 30)
# Salida:
# ID objeto: 140735524251008
# Dir memoria: 0x7f8b3c0b3c00

# Llamar al método
person.print_info()
# Salida:
# Name: John, Age: 30
