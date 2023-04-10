from operators import Operate
class InputList:
    def __init__(self, input_prob,input_prob_list=[]):
        self.input_prob = input_prob
        self.input_prob_list = input_prob_list
    
    def create_list(self,input_prob):
        operators_list = ["+","-","x","/","(",")"]
        for i in input_prob:
            if i not in operators_list:
                self.input_prob_list.append(int(i))
            elif i in operators_list:
                self.input_prob_list.append(i)
    def bidmas(self,input_prob_list):
        