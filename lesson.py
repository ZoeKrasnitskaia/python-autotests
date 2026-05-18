# Создайте класс прямоугольник — Rectangle.
# Метод __init__ принимает две точки — левый верхний и правый нижний угол.
# Каждая точка представлена экземпляром класса Point.
# Реализуйте методы вычисления площади и периметра прямоугольника.
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def calculate_plo(self):
        width = abs(self.point1.x - self.point2.x)
        height = abs(self.point1.y - self.point2.y)
        return width * height

    def perimeter(self):
        width = abs(self.point1.x - self.point2.x)
        height = abs(self.point1.y - self.point2.y)
        return 2 * (width + height)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0, 10) # Левая верхняя точка
p2 = Point(5, 0)  # Правая нижняя точка

rect = Rectangle(p1, p2)

print(f"Периметр: {rect.perimeter()}")
print(f"Площадь: {rect.calculate_plo()}")