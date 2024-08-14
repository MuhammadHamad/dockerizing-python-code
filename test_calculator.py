import unittest
from calculator import get_number, add, subtract, multiply, divide, exponentiate, perform_operation

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error: Division by zero is not allowed.")

    def test_exponentiate(self):
        self.assertEqual(exponentiate(2, 3), 8)
        self.assertEqual(exponentiate(5, 0), 1)

    def test_perform_operation(self):
        self.assertEqual(perform_operation(4, 2, "+"), 6)
        self.assertEqual(perform_operation(10, 3, "-"), 7)
        self.assertEqual(perform_operation(3, 5, "*"), 15)
        self.assertEqual(perform_operation(8, 2, "/"), 4)
        self.assertEqual(perform_operation(2, 0, "/"), "Error: Division by zero is not allowed.")
        self.assertEqual(perform_operation(3, 4, "^"), 81)
        self.assertEqual(perform_operation(5, 2, "%"), "Error: Unknown operation.")

if __name__ == '__main__':
    unittest.main()