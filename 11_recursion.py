# ==============================
# RECURSION: FACTORIAL AND POWER OF A NUMBER
# Ejemplos de funciones recursivas para:
# 1. Factorial de un número
# 2. Potencia de un número
# ==============================

# ------------------------------
# 1. Factorial de un número
# ------------------------------
def factorial(n):
    """
    Calcula el factorial de n usando recursividad.
    n! = n * (n-1) * (n-2) * ... * 1
    Caso base: factorial(0) = 1, factorial(1) = 1

    Ejemplo para n = 5:
    factorial(5)
      = 5 * factorial(4)
        = 5 * (4 * factorial(3))
          = 5 * (4 * (3 * factorial(2)))
            = 5 * (4 * (3 * (2 * factorial(1))))
              = 5 * (4 * (3 * (2 * 1)))
              = 5 * (4 * (3 * 2))
              = 5 * (4 * 6)
              = 5 * 24
              = 120
    """
    if n == 0 or n == 1:  # Caso base
        return 1
    return n * factorial(n - 1)  # Llamada recursiva

# Ejemplo:
num = 5
print(f"Factorial de {num} es: {factorial(num)}")
# Salida: Factorial de 5 es: 120


# ------------------------------
# 2. Potencia de un número
# ------------------------------
def power(base, exponent):
    """
    Calcula la potencia base^exponent usando recursividad.
    Caso base: cualquier número ^ 0 = 1

    Ejemplo para base=2, exponent=3:
    power(2, 3)
      = 2 * power(2, 2)
        = 2 * (2 * power(2, 1))
          = 2 * (2 * (2 * power(2, 0)))
            = 2 * (2 * (2 * 1))
            = 2 * (2 * 2)
            = 2 * 4
            = 8
    """
    if exponent == 0:  # Caso base
        return 1
    return base * power(base, exponent - 1)  # Llamada recursiva

# Ejemplo:
b = 2
e = 3
print(f"{b} elevado a la {e} es: {power(b, e)}")
# Salida: 2 elevado a la 3 es: 8
