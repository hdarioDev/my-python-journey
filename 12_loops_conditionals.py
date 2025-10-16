# ==============================
# LOOPS AND CONDITIONALS IN PYTHON
# Ejemplos básicos de condicionales (if, elif, else),
# bucles (for, while), control de flujo (break, continue),
# bucles anidados y match-case (similar a switch, Python 3.10+).
# ==============================

print("=== CONDICIONALES ===")

# Ejemplo 1: if básico
age = 18
if age >= 18:
    print("Eres mayor de edad")
    # Salida: Eres mayor de edad

# Ejemplo 2: if-else
temperature = 25
if temperature > 30:
    print("Hace calor")
else:
    print("No hace calor")
    # Salida: No hace calor

# Ejemplo 3: if-elif-else
score = 85
if score >= 90:
    print("Excelente")
elif score >= 70:
    print("Aprobado")
else:
    print("Reprobado")
    # Salida: Aprobado

print("\n" + "="*50 + "\n")

# ==============================
# BUCLE FOR
# ==============================

print("=== BUCLE FOR ===")

# Recorrer lista
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Fruta: {fruit}")
# Salida:
# Fruta: apple
# Fruta: banana
# Fruta: orange

# Recorrer rango de números
for i in range(1, 6):
    print(f"Número: {i}")
# Salida:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Número: 5

# Recorrer lista con índice usando enumerate()
for index, fruit in enumerate(fruits):
    print(f"Índice {index}: {fruit}")
# Salida:
# Índice 0: apple
# Índice 1: banana
# Índice 2: orange

print("\n" + "="*50 + "\n")

# ==============================
# BUCLE WHILE
# ==============================

print("=== BUCLE WHILE ===")

# Contar de 1 a 5
counter = 1
while counter <= 5:
    print(f"Contador: {counter}")
    counter += 1
# Salida:
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4
# Contador: 5

# Ejemplo de while con continue y break
number = 0
while True:
    number += 1
    if number == 3:
        print("Saltando número 3")
        continue  # Salta el resto de esta iteración
    if number > 5:
        break  # Rompe el bucle
    print(f"Número: {number}")
# Salida:
# Número: 1
# Número: 2
# Saltando número 3
# Número: 4
# Número: 5

print("\n" + "="*50 + "\n")

# ==============================
# BUCLES ANIDADOS
# ==============================

print("=== BUCLES ANIDADOS ===")

for i in range(1, 4):  # Filas
    for j in range(1, 4):  # Columnas
        print(f"({i},{j})", end=" ")
    print()
# Salida:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)

print("\n" + "="*50 + "\n")

# ==============================
# SWITCH-LIKE STATEMENT (MATCH-CASE) - Python 3.10+
# ==============================

print("=== MATCH-CASE (SIMILAR A SWITCH) ===")

# Ejemplo 1: día de la semana por número
day = 3
match day:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Día inválido")
# Salida: Miércoles

# Ejemplo 2: agrupar múltiples valores en un mismo case
match day:
    case 1 | 2 | 3:
        print("Es inicio de semana")
    case 4 | 5:
        print("Es casi fin de semana")
    case 6 | 7:
        print("Es fin de semana")
    case _:
        print("Día inválido")
# Salida: Es inicio de semana

# Ejemplo 3: match con patrones y guardas (condición extra)
user = {"role": "admin", "active": True}
match user:
    case {"role": "admin", "active": True}:
        print("Acceso total para admin activo")
    case {"role": "admin"}:
        print("Admin inactivo: acceso restringido")
    case {"role": "user", "active": True}:
        print("Acceso estándar para usuario activo")
    case _:
        print("Rol desconocido o datos incompletos")
# Salida: Acceso total para admin activo

print("\n=== FIN DEL PROGRAMA ===")
