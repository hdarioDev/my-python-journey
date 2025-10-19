# ==============================
# ABSTRACT BASE CLASS (ABC): BASIC EXAMPLE
# ABC define una plantilla que las clases hijas DEBEN seguir
# No se puede instanciar directamente, solo heredar de ella
# Usa @abstractmethod para definir métodos obligatorios
# ==============================

from abc import ABC, abstractmethod


# Clase abstracta
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Método abstracto - DEBE ser implementado por clases hijas"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Método abstracto - DEBE ser implementado por clases hijas"""
        pass
    
    def description(self):
        """Método concreto - puede ser usado por todas las clases hijas"""
        return f'Shape with area: {self.area()}'


# Clases concretas que implementan los métodos abstractos
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


# Ejemplo de uso
if __name__ == '__main__':
    # Esto daría error:
    # shape = Shape()  # TypeError: Can't instantiate abstract class
    
    rect = Rectangle(5, 3)
    print(f'Rectangle - Area: {rect.area()}, Perimeter: {rect.perimeter()}')
    print(rect.description())
    
    circle = Circle(4)
    print(f'\nCircle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}')
    print(circle.description())
