import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertGreater(10, 3, "should be true")
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 1), 6)
        self.assertEqual(self.calc.add(10, 7), 17)

    # Remember to write additional test methods for subtract, multiply, and divide.
    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(20,10),10)
        self.assertEqual(self.calc.subtract(-1, -7), 6)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 3), 30)

    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(50, 10), 5)
        self.assertEqual(self.calc.divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()
