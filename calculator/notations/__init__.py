class InvalidCharacterError(Exception):
    def __init__(self,index):
        self.index = index
class InvalidParenthesesError(Exception):
    pass
class InvalidExpressionError(Exception):
    pass 
class InvalidOperationsError(Exception):
    pass      
class InvalidRpnError(Exception):
    pass