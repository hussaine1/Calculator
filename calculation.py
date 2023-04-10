from operator import pow, truediv, mul, add, sub
class Calculation:
    operators = {
    '+': add,
    '-': sub,
    '*': mul,
     '/': truediv
    }
    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    @staticmethod
    def calculate(input):
        if input.isdigit():
            return float(input)
        elif Calculation.is_float(input)==True:
            return float(input)
        for c in Calculation.operators.keys():
            left, operator, right = input.partition(c)
            if operator in Calculation.operators:
                return Calculation.operators[operator](Calculation.calculate(left), Calculation.calculate(right))
    
    