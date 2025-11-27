import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        '''Проверяет вычисление площади круга с нулевым радиусом.

        Параметры на вход:
        r = 0 (float) - нулевой радиус круга

        Ожидаемый результат:
        area = 0 (float) - площадь круга должна быть равна нулю
        '''
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_normal_radius_area(self):
        '''Проверяет вычисление площади круга с положительным радиусом.

        Параметры на вход:
        r = 5 (float) - радиус круга

        Ожидаемый результат:
        area = math.pi * 25 (float) - площадь круга по формуле πR²
        '''
        res = circle_area(5)
        self.assertEqual(res, math.pi * 25)

    def test_zero_radius_perimeter(self):
        '''Проверяет вычисление периметра круга с нулевым радиусом.

        Параметры на вход:
        r = 0 (float) - нулевой радиус круга

        Ожидаемый результат:
        perimeter = 0 (float) - периметр круга должен быть равен нулю
        '''
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_normal_radius_perimeter(self):
        '''Проверяет вычисление периметра круга с положительным радиусом.

        Параметры на вход:
        r = 3 (float) - радиус круга

        Ожидаемый результат:
        perimeter = 2 * math.pi * 3 (float) - периметр круга по формуле 2πr
        '''
        res = circle_perimeter(3)
        self.assertEqual(res, 2 * math.pi * 3)


class TriangleTestCase(unittest.TestCase):
    def test_normal_triangle_area(self):
        '''Проверяет вычисление площади треугольника с нормальными параметрами.

        Параметры на вход:
        a = 10 (float) - основание треугольника
        h = 5 (float) - высота треугольника

        Ожидаемый результат:
        area = 25 (float) - площадь треугольника по формуле (a * h) / 2
        '''
        res = triangle_area(10, 5)
        self.assertEqual(res, 25)

    def test_zero_base_area(self):
        '''Проверяет вычисление площади треугольника с нулевым основанием.

        Параметры на вход:
        a = 0 (float) - нулевое основание треугольника
        h = 5 (float) - высота треугольника

        Ожидаемый результат:
        area = 0 (float) - площадь треугольника должна быть равна нулю
        '''
        res = triangle_area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        '''Проверяет вычисление площади треугольника с нулевой высотой.

        Параметры на вход:
        a = 10 (float) - основание треугольника
        h = 0 (float) - нулевая высота треугольника

        Ожидаемый результат:
        area = 0 (float) - площадь треугольника должна быть равна нулю
        '''
        res = triangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_normal_triangle_perimeter(self):
        '''Проверяет вычисление периметра треугольника с нормальными сторонами.

        Параметры на вход:
        a = 3 (float) - первая сторона треугольника
        b = 4 (float) - вторая сторона треугольника
        c = 5 (float) - третья сторона треугольника

        Ожидаемый результат:
        perimeter = 12 (float) - периметр треугольника по формуле a + b + c
        '''
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_side_perimeter(self):
        '''Проверяет вычисление периметра треугольника с нулевой стороной.

        Параметры на вход:
        a = 0 (float) - нулевая сторона треугольника
        b = 0 (float) - вторая сторона треугольника
        c = 0 (float) - третья сторона треугольника

        Ожидаемый результат:
        perimeter = 0 (float) - периметр треугольника как сумма сторон
        '''
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)


class SquareTestCase(unittest.TestCase):
    def test_normal_square_area(self):
        '''Проверяет вычисление площади квадрата с нормальной стороной.

        Параметры на вход:
        a = 5 (float) - сторона квадрата

        Ожидаемый результат:
        area = 25 (float) - площадь квадрата по формуле a²
        '''
        res = square_area(5)
        self.assertEqual(res, 25)

    def test_zero_square_area(self):
        '''Проверяет вычисление площади квадрата с нулевой стороной.

        Параметры на вход:
        a = 0 (float) - нулевая сторона квадрата

        Ожидаемый результат:
        area = 0 (float) - площадь квадрата должна быть равна нулю
        '''
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_normal_square_perimeter(self):
        '''Проверяет вычисление периметра квадрата с нормальной стороной.

        Параметры на вход:
        a = 5 (float) - сторона квадрата

        Ожидаемый результат:
        perimeter = 20 (float) - периметр квадрата по формуле 4a
        '''
        res = square_perimeter(5)
        self.assertEqual(res, 20)

    def test_zero_square_perimeter(self):
        '''Проверяет вычисление периметра квадрата с нулевой стороной.

        Параметры на вход:
        a = 0 (float) - нулевая сторона квадрата

        Ожидаемый результат:
        perimeter = 0 (float) - периметр квадрата должен быть равен нулю
        '''
        res = square_perimeter(0)
        self.assertEqual(res, 0)


class RectangleTestCase(unittest.TestCase):
    def test_zero_rectangle_area(self):
        '''Проверяет вычисление площади прямоугольника с нулевой шириной.

        Параметры на вход:
        a = 10 (float) - высота прямоугольника
        b = 0 (float) - нулевая ширина прямоугольника

        Ожидаемый результат:
        area = 0 (float) - площадь прямоугольника должна быть равна нулю
        '''
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_normal_rectangle_area(self):
        '''Проверяет вычисление площади квадратного прямоугольника.

        Параметры на вход:
        a = 10 (float) - высота прямоугольника
        b = 10 (float) - ширина прямоугольника

        Ожидаемый результат:
        area = 100 (float) - площадь прямоугольника по формуле a * b
        '''
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)

    def test_normal_rectangle_perimeter(self):
        '''Проверяет вычисление периметра прямоугольника с нормальными сторонами.

        Параметры на вход:
        a = 10 (float) - высота прямоугольника
        b = 20 (float) - ширина прямоугольника

        Ожидаемый результат:
        perimeter = 60 (float) - периметр прямоугольника по формуле 2(a + b)
        '''
        res = rectangle_perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_zero_rectangle_perimeter(self):
        '''Проверяет вычисление периметра прямоугольника с нулевыми сторонами.

        Параметры на вход:
        a = 0 (float) - нулевая высота прямоугольника
        b = 0 (float) - нулевая ширина прямоугольника

        Ожидаемый результат:
        perimeter = 0 (float) - периметр прямоугольника должен быть равен нулю
        '''
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, 0)