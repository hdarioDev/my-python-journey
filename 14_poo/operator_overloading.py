# ==============================
# OPERATOR OVERLOADING: BASIC EXAMPLE
# Sobrecarga de operadores permite redefinir operadores como +, -, *, etc.
# __add__ sobrescribe el operador +
# __sub__ sobrescribe el operador -
# __mul__ sobrescribe el operador *
# ==============================


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Sobrecarga del operador +"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Sobrecarga del operador -"""
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'


# Ejemplo de uso
if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    
    # Usar operador + (llama a __add__)
    p3 = p1 + p2
    print(f'{p1} + {p2} = {p3}')  # Point(3, 4) + Point(1, 2) = Point(4, 6)
    
    # Usar operador - (llama a __sub__)
    p4 = p1 - p2
    print(f'{p1} - {p2} = {p4}')  # Point(3, 4) - Point(1, 2) = Point(2, 2)


# Ejemplo 2: Sobrecarga con clase Money
class Money:
    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        """Sumar dinero (solo si es la misma moneda)"""
        if self.currency != other.currency:
            raise ValueError('Cannot add different currencies')
        return Money(self.amount + other.amount, self.currency)
    
    def __str__(self):
        return f'{self.amount} {self.currency}'


if __name__ == '__main__':
    print('\n*** Money Example ***')
    m1 = Money(100, 'USD')
    m2 = Money(50, 'USD')
    
    m3 = m1 + m2
    print(f'{m1} + {m2} = {m3}')  # 100 USD + 50 USD = 150 USD
