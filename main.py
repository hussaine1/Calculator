from operators import Operate
from input import InputOperation
import tkinter as tk


while True:
    input_prob = input("Enter operation: (e.g 2x2)")
    item = InputOperation(input_prob)
    item.sorting_out(input_prob)
    first_try=Operate(item.num1,item.num2,item.operator)
    print(first_try.operation(item.num1,item.num2,item.operator))

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Programme Ended")
        break




    
