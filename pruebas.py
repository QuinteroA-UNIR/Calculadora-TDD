import unittest
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()

    def test_suma_enteros(self):
        self.assertEqual(4, self.calculator.add(2,2))

if __name__ == "__main__":
    unittest.main()