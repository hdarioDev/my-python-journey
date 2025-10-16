# ==============================
# SETS
# Un set (conjunto) es una colección desordenada y sin elementos duplicados.
# - Sirve para eliminar duplicados.
# - Permite hacer operaciones de conjuntos (unión, intersección, diferencia).
# - No tiene índice (no se accede por posición).
# ==============================

# Crear un set
my_set = {1, 2, 3}
other_set = set(("a", "b", "c"))  # Usando constructor set()

# Agregar y eliminar elementos
my_set.add(4)         # Agregar un elemento
my_set.remove(2)      # Eliminar un elemento (error si no existe)
my_set.discard(10)    # Eliminar sin error si no existe

# ==============================
# Operaciones de conjuntos
# ==============================

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Unión → {1, 2, 3, 4, 5}
print(a & b)   # Intersección → {3}
print(a - b)   # Diferencia → {1, 2}
print(b - a)   # Diferencia → {4, 5}
print(a ^ b)   # Diferencia simétrica → {1, 2, 4, 5}

# ==============================
# Verificar pertenencia
# ==============================
print(2 in a)  # True
print(7 in a)  # False

# ==============================
# Ejemplo: encontrar elementos comunes entre dos grupos
# ==============================
math_students = {"Ana", "Luis", "Pedro"}
physics_students = {"Luis", "Pedro", "Maria"}

common_students = math_students & physics_students
print(common_students)  # {'Luis', 'Pedro'}
