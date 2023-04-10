from calculation import Calculation


while True:
    calc = input("Type calculation:\n")
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
