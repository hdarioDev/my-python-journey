# ==============================
# MULTIPLE INHERITANCE: BASIC EXAMPLE
# Herencia múltiple permite que una clase herede de múltiples clases padre
# Sintaxis: class Hijo(Padre1, Padre2, Padre3)
# ==============================

# Clase padre 1
class GeometricShape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


# Clase padre 2
class Color:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return f'El color es {self.color}'


# Clase hija con herencia múltiple
class Square(GeometricShape, Color):
    def __init__(self, side, color):
        # Inicializar ambas clases padre
        GeometricShape.__init__(self, side, side)
        Color.__init__(self, color)
    
    def __str__(self):
        return f'Square: side={self.width}, color={self.color}, area={self.area()}'


# Ejemplo de uso
if __name__ == '__main__':
    square = Square(5, 'red')
    print(square)  # Square: side=5, color=red, area=25
    print(square.get_color())  # El color es red
    print(f'Área: {square.area()}')  # Área: 25
