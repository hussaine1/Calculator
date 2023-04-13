from operator import pow, truediv, mul, add, sub
class Calculation:
    operators = {
    '+': add,
    '-': sub,
    '*': mul,
     '/': truediv,
     '^': pow
    }
    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    @staticmethod
    def bracket_input(check_input):
        left_brack_list=[]
        right_brack_list=[]
        #if "(" or ")" not in check_input:
            #return Calculation.calculate(check_input)
        # creating lists and putting in all the brackets that appear in the input
        for element in range(len(check_input)):
            if check_input[element] == "(":
                left_brack_list.append(element)
            elif check_input[element] == ")":
                right_brack_list.append(element)
        # the next block finds the starting and ending bracket of the deepest bracket calculation
        # this is because this should be calculated first
        
        # the deepest brackets have to be computed first. 
        # the right-most left bracket in the deepest left bracket. 
        # the deepest right bracket is more complicated to find depending on the input
        # eg (()-())
        starting_brack = left_brack_list[-1]
        if min(right_brack_list) < max(left_brack_list):
            temp_right_brack_list=[]
            for i in right_brack_list:
                if i < left_brack_list[-1]:
                    pass
                elif i > left_brack_list[-1]:
                    temp_right_brack_list.append(i)
            ending_brack =temp_right_brack_list[0]
        elif min(right_brack_list) > max(left_brack_list):
            ending_brack = right_brack_list[0]
            
                    
        extracted = check_input[starting_brack+1:ending_brack]
        if starting_brack == 0:
            check_input = "(" + check_input[ending_brack:]
        else: 
            check_input = check_input[0:starting_brack+1] + check_input[ending_brack:]
        check_input = check_input.replace("()",str(Calculation.calculate(extracted)))
        return check_input
        
        # now can remove the starting bracket and ending bracket and everything in between
        # then pass this extracted operation in the calculate method.
        # then put the answer back in to the input string and loop until no more brackets left.
        

                
        
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
    
    