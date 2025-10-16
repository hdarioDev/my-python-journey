# ==============================
# LISTS
# Una lista es una colección ordenada, modificable y que puede contener duplicados.
# - Mantiene el orden de inserción.
# - Puede contener cualquier tipo de dato.
# - Es mutable (puede cambiarse después de creada).
# ==============================

# Crear una lista
fruits = ["apple", "banana", "orange", "pear"]
print("Lista original:", fruits)  # ['apple', 'banana', 'orange', 'pear']
print()

# Acceder a elementos
print("Primer elemento:", fruits[0])    # apple
print("Último elemento:", fruits[-1])   # pear
print()

# Agregar y modificar elementos
numbers = [10, 20, 30]
numbers.append(40)        # Agregar al final
numbers.insert(1, 15)     # Insertar en una posición específica
numbers.remove(20)        # Eliminar por valor
last_value = numbers.pop()  # Eliminar último elemento (y retornarlo)
numbers.sort()            # Ordenar (en su lugar)
numbers.reverse()         # Invertir el orden

# Insertar en una posición específica en otra lista
fruits = ["apple", "banana", "orange", "pear"]
fruits.insert(1, "kiwi")
print("Después de insertar 'kiwi' en la posición 1:", fruits)
# ['apple', 'kiwi', 'banana', 'orange', 'pear']
print()

# Recorrer una lista
print("Recorriendo la lista:")
for fruit in fruits:
    print("-", fruit)
print()

# Verificar si un elemento está en la lista
if "pear" in fruits:
    print("'pear' está en la lista")
else:
    print("'pear' no está en la lista")
print()

# Obtener la cantidad de elementos
print("Cantidad de frutas:", len(fruits))  # 5
print()

# ==============================
# Ejemplos de ordenamiento
# ==============================

numbers = [5, 2, 9, 1, 7]
print("Lista original de números:", numbers)  # [5, 2, 9, 1, 7]

# Ordenar de menor a mayor (in place)
numbers.sort()
print("Ordenada de menor a mayor:", numbers)  # [1, 2, 5, 7, 9]

# Ordenar de mayor a menor (in place)
numbers.sort(reverse=True)
print("Ordenada de mayor a menor:", numbers)  # [9, 7, 5, 2, 1]

# Usar sorted() para obtener una nueva lista ordenada (sin modificar la original)
numbers = [5, 2, 9, 1, 7]
new_list = sorted(numbers)
print("Original después de sorted():", numbers)   # [5, 2, 9, 1, 7]
print("Nueva lista ordenada:", new_list)          # [1, 2, 5, 7, 9]
