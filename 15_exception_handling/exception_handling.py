# ==============================
# EXCEPTION HANDLING: BASIC CONCEPTS
# Manejo de excepciones permite manejar errores de manera controlada
# Se puede capturar cualquier excepción con 'Exception' o 'BaseException'
# ==============================

# Nota: Siempre es mejor capturar excepciones específicas en lugar de Exception/BaseException
# a menos que sea realmente necesario, ya que podrías ocultar errores inesperados
# BaseException es la clase base de todas las excepciones, incluyendo SystemExit y KeyboardInterrupt
# Exception es la clase base para la mayoría de las excepciones

# Some Exceptions : TypeError, ValueError, ZeroDivisionError, IndexError, KeyError, FileNotFoundError, ImportError, NameError, AttributeError

# 1. Basic try-except (with BaseException and Exception)
try:
    # Esto lanzará una excepción
    result = 10 / 0
except BaseException as e:  # Captura cualquier excepción (incluyendo SystemExit, KeyboardInterrupt)
    # Output: Error (BaseException): division by zero
    print(f"Error (BaseException): {e}")

try:
    result = 10 / 0
except Exception as e:  # Captura la mayoría de las excepciones (recomendado para casos generales)
    # Output: Error (Exception): division by zero
    print(f"Error (Exception): {e}"

# 2. Basic try-except with specific exception
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 2. Multiple exceptions
try:
    # This will raise a ValueError
    number = int("not_a_number")
except (ValueError, TypeError) as e:
    # Output: Invalid input: invalid literal for int() with base 10: 'not_a_number'
    print(f"Invalid input: {e}")

# 3. Else and Finally

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # Output when b is 0: Cannot divide by zero
        return "Cannot divide by zero"
    else:
        # Output when no exception: Result is 5.0
        return f"Result is {result}"
    finally:
        # This will always print, even if there's a return statement
        print("This always executes")  # Output: This always executes

print(divide(10, 2))
print(divide(10, 0))

# 4. Raising custom exceptions
def check_age(age):
    if age < 0:
        # This will be raised when age is negative
        raise ValueError("Age cannot be negative")
    elif age < 18:
        return "You are a minor"
    else:
        return "You are an adult"

try:
    print(check_age(-5))  # This will raise ValueError
except ValueError as e:
    # Output: Error: Age cannot be negative
    print(f"Error: {e}")

# 5. Custom exceptions
class InvalidEmailError(Exception):
    """Raised when the email format is invalid"""
    pass

def validate_email(email):
    if "@" not in email:
        # This will be raised when email doesn't contain '@'
        raise InvalidEmailError("Invalid email format")
    return "Email is valid"

try:
    # Output: Email is valid
    print(validate_email("test@example.com"))
    # This will raise InvalidEmailError
    print(validate_email("invalid-email"))
except InvalidEmailError as e:
    # Output: Validation error: Invalid email format
    print(f"Validation error: {e}")
