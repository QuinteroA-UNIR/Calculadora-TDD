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
            result += op1
        return result