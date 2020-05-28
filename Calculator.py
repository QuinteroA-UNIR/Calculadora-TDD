class Calculator:
    def add(self, op1, op2):
        if (op1 < 0 or op2 < 0):
            raise ArithmeticError("No se permiten valores negativos")
        return op1 + op2
    def minus(self, op1, op2):
        if (op1 < 0 or op2 < 0):
            raise ArithmeticError("No se permiten valores negativos")
        return op1 - op2
    def multiple(self, op1, op2):
        if (op1 < 0 or op2 < 0):
            raise ArithmeticError("No se permiten valores negativos")
        result = 0
        for i in range(op2):
            result = self.add(result,op1)
        return result
    def divide(self, n, d):
        if (d <= 0 or n < 0):
            raise ArithmeticError("No se permiten valores negativos")
        quotient = 0
        residue = n
        while residue >= d:
            quotient = self.add(quotient, 1)
            residue = self.minus(residue, d)
        return (quotient, residue)
    def sqrt(self, op):
        a = self.multiple(5, op)
        b = 5
        while b < 10000000:
            if (a >= b):
                a = self.minus(a,b)
                b = self.add(b, 10)
            else:
                a = self.multiple(a, 100)
                b = self.multiple(b, 10)
                b = self.minus(b, 45)
        b = self.minus(b, 5)
        return self.divide(b, 10000000)

