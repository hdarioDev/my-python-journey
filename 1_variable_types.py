# ==============================
# VARIABLE TYPES IN PYTHON
# Tipos de variables en Python y ejemplos básicos de cada uno.
# ==============================

# 1. NÚMEROS (NUMBERS)
print("1. NUMBERS:")
# Enteros (int)
age = 25
print(f"Entero (int): {age} - Tipo: {type(age)}")  # Entero (int): 25 - Tipo: <class 'int'>

# Flotantes (float)
height = 1.75
print(f"Flotante (float): {height} - Tipo: {type(height)}")  # Flotante (float): 1.75 - Tipo: <class 'float'>
print()

# 2. CADENAS DE TEXTO (STRINGS)
print("2. STRINGS:")
first_name = "John"
last_name = 'Doe'
description = """Este es un texto
de varias líneas"""

print(f"Cadena simple: '{first_name}' - Tipo: {type(first_name)}")         # 'John' - Tipo: <class 'str'>
print(f"Cadena con comillas simples: '{last_name}' - Tipo: {type(last_name)}")  # 'Doe' - Tipo: <class 'str'>
print(f"Cadena multilínea: {repr(description)} - Tipo: {type(description)}")   # 'Este es un texto\nde varias líneas' - Tipo: <class 'str'>
print("\n" + "="*50 + "\n")

# 3. BOOLEANOS (BOOLEANS)
print("3. BOOLEANS:")
is_student = True
has_job = False
print(f"Verdadero: {is_student} - Tipo: {type(is_student)}")  # True - Tipo: <class 'bool'>
print(f"Falso: {has_job} - Tipo: {type(has_job)}")            # False - Tipo: <class 'bool'>
print("\n" + "="*50 + "\n")

# 4. LISTAS (LISTS)
print("4. LISTS:")
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["text", 42, True, 3.14]

print(f"Lista de frutas: {fruits} - Tipo: {type(fruits)}")      # ['apple', 'banana', 'orange'] - Tipo: <class 'list'>
print(f"Lista de números: {numbers} - Tipo: {type(numbers)}")   # [1, 2, 3, 4, 5] - Tipo: <class 'list'>
print(f"Lista mixta: {mixed_list} - Tipo: {type(mixed_list)}")  # ['text', 42, True, 3.14] - Tipo: <class 'list'>
print("\n" + "="*50 + "\n")

# 5. TUPLAS (TUPLES)
print("5. TUPLES:")
coordinates = (10, 20)
colors = ("red", "green", "blue")

print(f"Coordenadas: {coordinates} - Tipo: {type(coordinates)}")  # (10, 20) - Tipo: <class 'tuple'>
print(f"Colores: {colors} - Tipo: {type(colors)}")                 # ('red', 'green', 'blue') - Tipo: <class 'tuple'>
print("\n" + "="*50 + "\n")

# 6. DICCIONARIOS (DICTIONARIES)
print("6. DICTIONARIES:")
person = {
    "name": "Anna",
    "age": 30,
    "city": "Madrid"
}
print(f"Diccionario de persona: {person} - Tipo: {type(person)}")
# {'name': 'Anna', 'age': 30, 'city': 'Madrid'} - Tipo: <class 'dict'>
print("\n" + "="*50 + "\n")

# 7. CONJUNTOS (SETS)
print("7. SETS:")
unique_numbers = {1, 2, 3, 4, 5}
letters = {"a", "b", "c"}

print(f"Set de números: {unique_numbers} - Tipo: {type(unique_numbers)}")  # {1, 2, 3, 4, 5} - Tipo: <class 'set'>
print(f"Set de letras: {letters} - Tipo: {type(letters)}")                  # {'a', 'b', 'c'} - Tipo: <class 'set'>
print("\n" + "="*50 + "\n")

# 8. NONE TYPE
print("8. NONE TYPE:")
empty_value = None
print(f"Valor None: {empty_value} - Tipo: {type(empty_value)}")  # None - Tipo: <class 'NoneType'>
print("\n" + "="*50 + "\n")

# 9. CONVERSIONES DE TIPOS (TYPE CONVERSIONS)
print("9. TYPE CONVERSIONS:")
number_string = "123"
number_int = int(number_string)       # String → int
number_float = float(number_string)   # String → float

print(f"Cadena '{number_string}' convertida a int: {number_int}")       # 123
print(f"Cadena '{number_string}' convertida a float: {number_float}")   # 123.0

# Convertir número a string
age_number = 25
age_string = str(age_number)
print(f"Número {age_number} convertido a cadena: '{age_string}'")  # '25'
print("\n" + "="*50 + "\n")

# 10. VERIFICACIÓN DE TIPOS (TYPE CHECKING)
print("10. TYPE CHECKING:")
value = 42
print(f"¿Es {value} un entero? {isinstance(value, int)}")         # True
print(f"¿Es {value} una cadena? {isinstance(value, str)}")        # False
print(f"¿Es {value} un número? {isinstance(value, (int, float))}")  # True
print("\n=== END OF PROGRAM ===")
