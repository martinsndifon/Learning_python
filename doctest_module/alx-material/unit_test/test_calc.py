import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        """The arguments to assertEqual are the function from calc
        with the required arguments and the actual result expected"""
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        self.assertRaises(ZeroDivisionError, calc.divide, 3, 0)
        """The above assertRaises method can also be written as:
        with self.assertRaises(ZeroDivisionError):
            calc.divide(3, 0)
        """


if  __name__ == "__main__":
    unittest.main()
