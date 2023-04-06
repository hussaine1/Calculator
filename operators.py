class Operate:
    def __init__(self,num1:int,num2:int,operator:str):
        #for now will only take inputs as ints
        #assert num1.is_integer(), f"first number ({num1}) is not and integer."
       # assert num2.is_integer(), f"second number ({num2}) is not and integer."

        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    @classmethod
    def operation(cls,num1,num2,operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "x":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "cannot divide by zero"
            else:
                return num1/num2
        else:
            return "Operator only takes the following inputs: +,-,x,/"
            