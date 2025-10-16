# ==============================
# TUPLES
# Una tupla es una colección ordenada y NO modificable.
# - Puede contener duplicados.
# - Mantiene el orden de los elementos.
# - Es útil para datos que no deben cambiar.
# ==============================

# Crear una tupla
fruits = ("apple", "banana", "orange", "pear")
print("Frutas:", fruits)

# Acceder a elementos por índice
print("Primer elemento:", fruits[0])    # apple
print("Último elemento:", fruits[-1])   # pear
print()

# Suma de elementos (solo si son numéricos)
numbers = (1, 2, 3, 4, 5)
total = sum(numbers)
print("Suma de sus elementos:", total)  # 15
print()

# Operaciones comunes con tuplas
tuple_example = (10, 20, 30)
print(tuple_example[0])         # Acceso por índice → 10
print(tuple_example.index(20))  # Índice de un valor → 1
print(tuple_example.count(10))  # Contar apariciones de un valor → 1
print()

# Definir una tupla sin paréntesis (tuple packing)
tuple_no_parentheses = "apple", "banana", "orange", "pear"
print("Tupla sin paréntesis:", tuple_no_parentheses)
print()

# Desempaquetar tupla (tuple unpacking)
person = ("Ana", 25)
name, age = person
print(name)  # Ana
