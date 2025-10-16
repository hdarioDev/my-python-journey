# ==============================
# STRING FORMATTING IN PYTHON
# Formateo y manipulación de cadenas en Python.
# ==============================

# 1. f-strings (Recomendado - Python 3.6+)
name = "Juan"
age = 30
print(f"1. Hola, me llamo {name} y tengo {age} años")
# Salida: Hola, me llamo Juan y tengo 30 años

# 2. .format() (Alternativa)
print("2. Hola, me llamo {} y tengo {} años".format(name, age))
# Salida: Hola, me llamo Juan y tengo 30 años

# ==============================
# Ejemplos útiles con f-strings
# ==============================

# - Números decimales con 2 decimales
price = 19.99
print(f"3. Precio: ${price:.2f}")
# Salida: Precio: $19.99

# - Operaciones dentro de f-string
print(f"4. 5 + 3 = {5 + 3}")
# Salida: 5 + 3 = 8

# - Texto en mayúsculas
print(f"5. {'hola'.upper()}")
# Salida: HOLA

# - Texto en minúsculas
print(f"6. {'HOLA'.lower()}")
# Salida: hola

# - Eliminar espacios en blanco
print(f"7. {'   hola   '.strip()}")
# Salida: hola

# ==============================
# Longitud de cadenas
# ==============================
text = "Python es genial"
print(f"8. La cadena '{text}' tiene {len(text)} caracteres")
# Salida: La cadena 'Python es genial' tiene 16 caracteres

# ==============================
# Manejo de subcadenas (Slicing)
# ==============================
phrase = "Aprendiendo Python"
print(f"9. Frase original: '{phrase}'")
# Salida: Frase original: 'Aprendiendo Python'

# Primeros 5 caracteres
print(f"   Primeros 5 caracteres: '{phrase[:5]}'")  # Apren

# Últimos 6 caracteres
print(f"   Últimos 6 caracteres: '{phrase[-6:]}'")  # Python

# Caracteres del índice 3 al 8
print(f"   Del índice 3 al 8: '{phrase[3:9]}'")  # endien

# Cada segundo carácter
print(f"   Cada segundo carácter: '{phrase[::2]}'")  # ApnindoPto

# ==============================
# Métodos útiles para subcadenas
# ==============================
word = "programación"
print(f"10. Palabra: '{word}'")

# Buscar si contiene una subcadena
if "gram" in word:
    print("   La palabra contiene 'gram'")  # Se muestra este mensaje

# Encontrar posición de una subcadena
position = word.find("gram")
print(f"   'gram' se encuentra en la posición: {position}")  # 3

# Reemplazar subcadenas
new_word = word.replace("gram", "GRAM")
print(f"   Reemplazando 'gram' por 'GRAM': '{new_word}'")  # proGRAMación

# Dividir cadena en subcadenas (split)
full_phrase = "Python es fácil de aprender"
words = full_phrase.split()
print(f"   Dividiendo '{full_phrase}' en palabras: {words}")
# ['Python', 'es', 'fácil', 'de', 'aprender']
print(f"   Primera palabra: '{words[0]}'")  # Python
print(f"   Última palabra: '{words[-1]}'")  # aprender
