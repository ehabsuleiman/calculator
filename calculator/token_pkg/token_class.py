from typing import NamedTuple
from calculator.utils import Types


"""
just a class to give a type and value of token for more readability
and to keep code consistent and robust

""" 

class Token(NamedTuple):
    type: str
    value: str


    #precedence in  math
    PRECEDENCE = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
    }


    #gets precedence of operator
    @property
    def precedence(self):
        if self.type == Types.OPERATOR:
           return self.PRECEDENCE[self.value]
    
    def is_less_precedent(self,token):
        if self.type == Types.OPERATOR:
            if self.precedence<=token.precedence:
                return True
        return False 
