# ==============================
# DICTIONARIES
# Un diccionario es una colección de pares clave:valor.
# - Cada clave es única.
# - Los valores se acceden rápidamente a través de su clave.
# - Las claves deben ser tipos inmutables (string, número, tupla).
# - Los diccionarios son mutables (pueden agregarse, modificarse y eliminarse elementos).
# ==============================

# Crear un diccionario
person = {
    "name": "Ana",
    "age": 25,
    "city": "Cochabamba"
}

# Otra forma de crear un diccionario
other = dict(name="Luis", age=30)

# Modificar o agregar elementos
person["age"] = 26            # Modificar un valor existente
person["profession"] = "Dev"  # Agregar un nuevo par clave:valor

# Obtener valores de forma segura
value = person.get("name")                       # Obtener valor por clave (None si no existe)
value = person.get("height", "No disponible")    # Obtener valor con un valor por defecto

# Eliminar elementos
del person["city"]             # Eliminar par clave:valor por clave
person.pop("profession")       # Eliminar clave y retornar su valor

# Vistas del diccionario (dinámicas, reflejan cambios en tiempo real)
keys_view = person.keys()      # Obtener solo las claves
values_view = person.values()  # Obtener solo los valores
items_view = person.items()    # Obtener pares (clave, valor) como tuplas

# Vaciar todo el diccionario
person.clear()                 # Elimina todos los elementos

# Recorrer un diccionario
for key, value in person.items():
    print(f"{key}: {value}")

# Desempaquetar valores del diccionario
info = {"a": 1, "b": 2}
a_val, b_val = info.values()
print(a_val, b_val)  # 1 2
