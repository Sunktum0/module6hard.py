import math

class Figure:
    sides_count = 0  # Количество сторон

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = []
        self.filled = False  # Публичный атрибут для заполненности

        self.set_color(*color)  # Устанавливаем цвет
        self.set_sides(*sides)  # Устанавливаем стороны

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1  # У круга 1 сторона

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)  # Рассчитываем радиус

    def get_square(self):
        return math.pi * (self.__radius ** 2)  # Площадь круга


class Triangle(Figure):
    sides_count = 3  # У треугольника 3 стороны

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Формула Герона


class Cube(Figure):
    sides_count = 12  # У куба 12 рёбер

    def __init__(self, color, side_length):
        super().__init__(color, side_length)
        # Здесь вместо изменения self.__sides мы можем вызывать set_sides
        self.set_sides(*(side_length for _ in range(self.sides_count)))  # Создаем список из 12 одинаковых сторон

    def get_volume(self):
        return self.get_sides()[0] ** 3  # Объем куба


# Тестирование
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (для круга это и есть длина):
print(len(circle1))  # 10, длина окружности (ожидается: 10)

# Проверка объема (куба):
print(cube1.get_volume())  # 216
