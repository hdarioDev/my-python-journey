# ==============================
# RANDOM NUMBERS AND CUSTOM UNIQUE ID GENERATION
# Demostración de uso de números aleatorios y creación de un ID único personalizado
# a partir de datos ingresados por el usuario y manipulación de cadenas.
# ==============================

from random import randint

# Número aleatorio entre 1 y 10 (incluye ambos extremos)
number = randint(1, 10)
print(f"El valor aleatorio es: {number}")
# Salida (ejemplo): El valor aleatorio es: 7

print("\n=== GENERAR ID MANUAL ===")
print("Generar ID manual")

# Entradas del usuario (se asume que el usuario introduce valores válidos)
# Ejemplo de entradas (comentado):
# name -> "Carlos"
# lastname -> "Pérez"
# year_of_birth -> "1992"

name = input("Ingrese el nombre: ")
lastname = input("Ingrese el apellido: ")
year_of_birth = input("Ingrese el año de nacimiento (YYYY): ")

# Tomar los 2 primeros caracteres del nombre y apellido en mayúsculas
two_first_characters_name = name[0:2].upper()          # "CA" si name = "Carlos"
two_first_characters_lastname = lastname[0:2].upper()  # "PE" si lastname = "Pérez"

# Tomar los 2 últimos dígitos del año de nacimiento
two_last_digits = year_of_birth[-2:]                   # "92" si year_of_birth = "1992"

# 4 dígitos aleatorios para asegurar unicidad básica
four_random_digits = str(randint(1000, 9999))         # "5381" (ejemplo)

# Construir el ID
unique_id = f"{two_first_characters_name}{two_first_characters_lastname}{two_last_digits}{four_random_digits}"

# Mostrar resultados
print(f"ID manual: {unique_id}")
print(f"{name} tu ID manual es: {unique_id}")

# Salida (ejemplo con las entradas comentadas arriba):
# ID manual: CAPE925381
# Carlos tu ID manual es: CAPE925381

# ==============================
# NOTAS:
# - Este ID es solo ilustrativo; no garantiza unicidad real en sistemas grandes.
# - Para producción, considerar validaciones:
#   * Verificar que name/lastname no estén vacíos (len >= 2).
#   * Verificar que year_of_birth tenga 4 dígitos y sea numérico.
#   * Usar UUID (módulo uuid) si necesitas identificadores realmente únicos.
# ==============================
