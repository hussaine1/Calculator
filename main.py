from calculation import Calculation


while True:
    calc = input("Type calculation:\n")
    if "(" or ")" in calc:
        # below loop is infinite, need to fix this 
        while "(" in calc:
            calc = Calculation.bracket_input(calc)  
        print("Answer: " + str(Calculation.calculate(calc)))
    elif "(" or ")" not in calc:
        print("Answer: " + str(Calculation.calculate(calc)))
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
