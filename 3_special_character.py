# ==============================
# SPECIAL CHARACTERS IN PYTHON
# Caracteres especiales en cadenas de texto y su uso.
# ==============================

print("=== BASIC SPECIAL CHARACTERS ===")
print('Hello \nWorld')              # \n: salto de línea → Hello (línea 1) / World (línea 2)
# Salida:
# Hello 
# World

print('\tPython \tis awesome!')     # \t: tabulación horizontal
# Salida:
#     Python     is awesome!

print('Juan\' "Perez"')             # \': comilla simple dentro de comillas simples
# Salida:
# Juan' "Perez"

print("Karla \" Gomez")             # \": comilla doble dentro de comillas dobles
# Salida:
# Karla " Gomez

print('Character \\ backslash')     # \\: imprimir una barra invertida
# Salida:
# Character \ backslash

print("\n" + "="*50 + "\n")

# ==============================
# CARACTERES ESPECIALES ÚTILES
# ==============================

# \b: retroceso (borra el carácter anterior en la consola)
print("Hello\b World")  
# Salida esperada visualmente:
# Hell World  (la 'o' de Hello se borra)

# \v: tabulación vertical
print("Line 1\vLine 2")
# Salida:
# Line 1
#        Line 2  (depende del terminal)

# Ejemplo: crear una tabla simple
print("ID\tName\t\tScore")
print("1\tJohn Doe\t95")
print("2\tJane Smith\t87")
# Salida:
# ID    Name        Score
# 1     John Doe    95
# 2     Jane Smith  87

# ==============================
# CADENAS MULTILÍNEA CON CARACTERES ESPECIALES
# ==============================
print("=== MULTILINE STRINGS WITH SPECIAL CHARACTERS ===")

# Usando triple comilla para texto multilínea con tabulaciones
message = """
Dear Customer,

Thank you for your purchase!

Order Details:
\tProduct: Python Course
\tPrice: $99.99
\tDiscount: 10%

Best regards,
The Team
"""
print(message)
# Salida:
# Dear Customer,
#
# Thank you for your purchase!
#
# Order Details:
#     Product: Python Course
#     Price: $99.99
#     Discount: 10%
#
# Best regards,
# The Team

print("=== END OF SPECIAL CHARACTERS DEMO ===")
