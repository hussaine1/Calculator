from operators import Operate
from input import InputOperation

input_prob = input("Enter operation: (e.g 2x2)")
item = InputOperation(input_prob)
item.sorting_out(input_prob)
first_try=Operate(item.num1,item.num2,item.operator)

print(first_try.operation(item.num1,item.num2,item.operator))
