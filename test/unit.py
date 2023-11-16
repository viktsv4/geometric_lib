import unittest
import rectangle
import circle
import square
import triange
class TestCase(unittest.TestCase):
    def test_rectangle_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)
        res = rectangle.area(3, "A")
        self.assertEqual(res,"Invalid input")
        res = rectangle.area(3, -1)
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(2.3, 3)
        self.assertEqual(res, "Invalid input")
        res = rectangle.area(3, True)
        self.assertEqual(res, "Invalid input")

    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(10, -1)
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(10, 2.3)
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(3, "A")
        self.assertEqual(res, "Invalid input")
        res = rectangle.perimeter(3, True)
        self.assertEqual(res, "Invalid input")

    def test_circle_area(self):
        res = circle.area(0)
        self.assertEqual(res, "Invalid input")
        res = circle.area(2)
        self.assertEqual(res, 12.56)
        res = circle.area("A")
        self.assertEqual(res, "Invalid input")
        res = circle.area(-4)
        self.assertEqual(res, "Invalid input")
        res = circle.area(12.888)
        self.assertEqual(res, "Invalid input")
        res = circle.area(True)
        self.assertEqual(res, "Invalid input")

    def test_circle_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(2)
        self.assertEqual(res, 12.56)
        res = circle.perimeter(2.9)
        self.assertEqual(res,"Invalid input" )
        res = circle.perimeter("A")
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(-4)
        self.assertEqual(res, "Invalid input")
        res = circle.perimeter(True)
        self.assertEqual(res, "Invalid input")

    def test_square_area(self):
        res = square.area(0)
        self.assertEqual(res, "Invalid input")
        res = square.area(2)
        self.assertEqual(res, 4)
        res = square.area("A")
        self.assertEqual(res, "Invalid input")
        res = square.area(-4)
        self.assertEqual(res, "Invalid input")
        res = square.area(1.7)
        self.assertEqual(res, "Invalid input")
        res = square.area(True)
        self.assertEqual(res, "Invalid input")

    def test_square_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(2)
        self.assertEqual(res, 8)
        res = square.perimeter("A")
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(-4)
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(9.3)
        self.assertEqual(res, "Invalid input")
        res = square.perimeter(True)
        self.assertEqual(res, "Invalid input")

    def test_triange_area(self):
        res = triange.area(0,10)
        self.assertEqual(res, "Invalid input")
        res = triange.area(2,3)
        self.assertEqual(res, 3)
        res = triange.area("A",3)
        self.assertEqual(res, "Invalid input")
        res = triange.area(2, -3)
        self.assertEqual(res, "Invalid input")
        res = triange.area(2.3,1)
        self.assertEqual(res, "Invalid input")
        res = triange.area(True,1)
        self.assertEqual(res, "Invalid input")

    def test_triange_perimeter(self):
        res = triange.perimeter(0,1,2)
        self.assertEqual(res, "Invalid input")
        res = triange.perimeter(3,4,5)
        self.assertEqual(res, 12)
        res = triange.perimeter("A",2,3)
        self.assertEqual(res, "Invalid input")
        res = triange.perimeter(-2,2, 3)
        self.assertEqual(res, "Invalid input")
        res = triange.perimeter(2.99, 2, 3)
        self.assertEqual(res, "Invalid input")
        res = triange.perimeter(True,2,3)
        self.assertEqual(res, "Invalid input")


if __name__ == '__main__':
    unittest.main()