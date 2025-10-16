# ==============================
# FUNCTIONS
# Bloque de código reutilizable que realiza una tarea.
# ==============================

# Función simple
def greet():
    print("¡Hello from the function!")

greet()  # Llamada

# Función con argumentos posicionales
def add(a, b):
    return a + b

print(add(3, 5))  # 8

# Función con argumentos con nombre
def introduce(name, age):
    print(f"I am {name} and I am {age} years old.")

introduce(age=25, name="Ana")

# Función con valor por defecto
def greet_name(name="guest"):
    print(f"Hello {name}")

greet_name()        # Hello guest
greet_name("Luis")  # Hello Luis

# Función con número variable de argumentos
def add_many(*args):
    return sum(args)

print(add_many(1, 2, 3, 4))  # 10

# Función con argumentos nombrados variables
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Ana", age=25)


# ==============================
# RECURSION
# Una función que se llama a sí misma para resolver un problema.
# Siempre necesita un caso base.
# ==============================

# Ejemplo: Factorial
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    return n * factorial(n - 1)  # Llamada recursiva

print(factorial(5))  # 120

# Ejemplo: Suma recursiva de una lista
def sum_list(numbers):
    if not numbers:  # Caso base: lista vacía
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4]))  # 10

# Ejemplo: Mostrar números del 1 al n
def show_numbers(n):
    if n > 0:                 # Caso base: cuando n llegue a 0 se detiene
        show_numbers(n - 1)   # Llamada recursiva antes de imprimir
        print(n)              # Se imprime al "regresar" de la recursión

show_numbers(5)
# Salida:
# 1
# 2
# 3
# 4
# 5
