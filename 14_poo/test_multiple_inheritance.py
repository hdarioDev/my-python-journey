"""
Test file for multiple_inheritance.py
Tests multiple instances of Square class
"""

from multiple_inheritance import Square


def test_multiple_instances():
    """Test creating and using multiple Square instances"""
    print('*** Test con múltiples instancias ***')
    
    # Create multiple squares
    square1 = Square(3, 'blue')
    square2 = Square(7, 'green')
    square3 = Square(10, 'yellow')
    
    squares = [square1, square2, square3]
    
    # Test each square
    for sq in squares:
        print(f'{sq} - {sq.get_color()}')
    
    # Verify areas
    print('\n*** Verificación de áreas ***')
    assert square1.area() == 9, 'Square1 area should be 9'
    assert square2.area() == 49, 'Square2 area should be 49'
    assert square3.area() == 100, 'Square3 area should be 100'
    print('✓ Todas las áreas son correctas')
    
    # Verify colors
    print('\n*** Verificación de colores ***')
    assert square1.color == 'blue', 'Square1 color should be blue'
    assert square2.color == 'green', 'Square2 color should be green'
    assert square3.color == 'yellow', 'Square3 color should be yellow'
    print('✓ Todos los colores son correctos')


if __name__ == '__main__':
    test_multiple_instances()
