#will need to take in an input list instead, so can do mulitple operations, eg. 5+5-6x4/2
#make a plan for this
class InputOperation:
    
    def __init__(self, input_prob,num1 =0,num2=0,operator=""):
        self.input_prob = input_prob
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def sorting_out(self, input_prob):
        operators_list = ["+","-","x","/"]
        input_prob = input_prob.replace(" ", "")
        for i in operators_list:
            if i in input_prob: 
                self.operator = i
                number_list = input_prob.split(i)
            else:
                pass
        self.num1 = int(number_list[0])
        self.num2 = int(number_list[1])
        