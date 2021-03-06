import unittest
from Calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()

    def test_suma_enteros(self):
        self.assertEqual(4, self.calculator.add(2,2))
    
    def test_suma_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculator.add, -2, 2)
    
    def test_suma_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculator.add, 2, -2)
    
    def test_suma_enteros_por_cero(self):
        self.assertEqual(2, self.calculator.add(2,0))
    
    def test_resta_enteros(self):
        self.assertEqual(0, self.calculator.minus(2,2))
    
    def test_resta_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculator.minus, -2, 2)
    
    def test_resta_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculator.minus, 2, -2)
    
    def test_resta_enteros_por_cero(self):
        self.assertEqual(2, self.calculator.minus(2,0))

    def test_mult_enteros(self):
        self.assertEqual(4, self.calculator.multiple(2,2))
    
    def test_mult_enteros_por_cero(self):
        self.assertEqual(0, self.calculator.multiple(2,0))
    
    def test_mult_enteros_por_uno(self):
        self.assertEqual(2, self.calculator.multiple(2,1))
    
    def test_mult_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculator.multiple, -2, 2)
    
    def test_mult_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculator.multiple, 2, -2)

    def test_div_enteros(self):
        self.assertEqual((1,0), self.calculator.divide(2,2))

    def test_div_enteros_1(self):
        self.assertEqual((2,0), self.calculator.divide(4,2))

    def test_div_enteros_2(self):
        self.assertEqual((1,1), self.calculator.divide(3,2))

    def test_div_enteros_3(self):
        self.assertEqual((0,0), self.calculator.divide(0,2))

    def test_div_enteros_4(self):
        self.assertEqual((0,20), self.calculator.divide(20,70))
    
    def test_div_enteros_por_uno(self):
        self.assertEqual((2,0), self.calculator.divide(2,1))
    
    def test_div_enteros_por_cero(self):
        self.assertRaises(ArithmeticError, self.calculator.divide, -2, 0)
    
    def test_div_invalido_negativo(self):
        self.assertRaises(ArithmeticError, self.calculator.divide, -2, 2)
    
    def test_div_invalido_negativo_2(self):
        self.assertRaises(ArithmeticError, self.calculator.divide, 2, -2)
    
    def test_sqrt(self):
        self.assertEqual((2,0), self.calculator.sqrt(4))
    
    def test_sqrt_2(self):
        self.assertEqual((1, 4142100), self.calculator.sqrt(2))
    
    def test_sqrt_3(self):
        self.assertEqual((1, 7320500), self.calculator.sqrt(3))
    
    def test_sqrt_negativo(self):
        self.assertRaises(ArithmeticError, self.calculator.sqrt, -2)
    
if __name__ == "__main__":
    unittest.main()