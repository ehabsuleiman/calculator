
from calculator.token_pkg.tokenizer import Tokenizer
from calculator.utils import Types, remove_brackets

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

class ConvertToPostfix():
    def __init__(self,exp):
        self.expression = exp

    def get_tokens(self):
        return Tokenizer(self.expression).tokens   

    #checks if the expression parentheses is valid
    def is_valid_parentheses(self):
        s = remove_brackets(''.join(self.expression))
        stack = []
        paren_dict = {")":"("}
        for char in list(s):
            if char in paren_dict.values():
                stack.append(char)
            elif char in paren_dict.keys():
                if stack == [] or paren_dict[char] != stack.pop():
                    raise InvalidParenthesesError
            else:
                    raise InvalidParenthesesError
        if stack == []:
            return True
        else:
            raise InvalidParenthesesError



    #validates the expression  
    def validate_expression(self):

        if self.expression == "":
            raise ValueError("An empty expression has been entered.")

        res = Tokenizer.split_postfix_expression(self.expression)

        #check for valid parantheses
        if not self.is_valid_parentheses():
            raise InvalidParenthesesError

        #check for operations are wrong
        
        res = self.get_tokens()

        for token in res:
            if token.type == Types.UNKNOWN:
                raise InvalidCharacterError(token.value)

        for i in range(len(res)-1):

            if res[i].type== Types.OPERATOR and res[i+1].type == Types.OPERATOR and res[i+1] != '-':
                raise InvalidOperationsError

        #first non left paren must be a number
        for token in res:
            if token.type == Types.LEFT_PAREN:
                continue
            elif token.type == Types.NUMBER:
                break
            else:
                raise InvalidOperationsError
        
        #last non right paren must be a number
        for token in reversed(res):
            if token.type == Types.RIGHT_PAREN:
                continue
            elif token.type == Types.NUMBER:
                break
            else:
                raise InvalidOperationsError
            

    def infix_to_postfix(self):

        """
        parameter: a list of tokens initiated with class tokenizer
        returns: a list of tokens with a postfix (RPN) Notations

        this function algorithim will use the shunting down algorithim to convert inftix to postfix notations
        you can read more about the function down below
        https://en.wikipedia.org/wiki/Shunting-yard_algorithm

        """ 

        self.validate_expression()

        #an operator array to be stacked
        operators = []

        #the ouptut in postfix
        output = []


        for token in self.get_tokens() :

            #if number we add to output
            if token.type == Types.NUMBER:
                output.append(token)

            #if type operator and not left parentheses and current token is less precedent then top operator we append to output
            #once done from while loop we push the operator to top of stack
            #handles precedence 
            elif token.type == Types.OPERATOR:
                while operators and operators[-1].type != Types.LEFT_PAREN and token.is_less_precedent(operators[-1]):
                    output.append(operators.pop())
                
                operators.append(token)
                    

            elif token.type == Types.LEFT_PAREN:
                operators.append(token)
            
            #handles right parantheses
            elif token.type == Types.RIGHT_PAREN:
                while operators and operators[-1].type != Types.LEFT_PAREN:
                    output.append(operators.pop())
                if operators == []:
                    raise InvalidParenthesesError
                operators.pop()



        # we push rest of operator to output
        while operators:
            if operators[-1].type == Types.LEFT_PAREN:
                raise InvalidParenthesesError 
            output.append(operators.pop()) 

        return output












