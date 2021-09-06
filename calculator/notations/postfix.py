
import operator
from calculator.utils import Types
from calculator.token_pkg.tokenizer import Tokenizer,Notaions
from calculator.notations import InvalidRpnError,InvalidCharacterError


class Postfix:
    def __init__(self,exp):
        self.expression = exp

    def get_tokens(self):
        return Tokenizer(self.expression,Notaions.POSTFIX).tokens   

    """
    parameter: an operation to do,first number, second number
    returns: a decimal with the evaluation of the operation

    """ 
    def do_operation(operation,num1,num2):
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            raise InvalidCharacterError

        if operation == '+':
            return  operator.add(num1,num2)
        elif operation == '-':
            return operator.sub(num1,num2)
        elif operation == '/':
            if num2 == 0:
                #handling division by zero
                raise ZeroDivisionError
            return operator.truediv(num1,num2)
        elif operation == '*':
            return operator.mul(num1, num2)
        elif operation == '%':
            return operator.mod(num1,num2)
        else:
            #operation not supported
            print('operation {operation} is not supported ')
            return 


    def validate_expression(self):

        if self.expression == "":
            raise ValueError("An empty expression has been entered.")

        stack = []

        for token in self.get_tokens():
            if token.type == Types.NUMBER :
                stack.append(token.value)
            elif token.type == Types.OPERATOR:
                if len(stack)<2:
                    raise InvalidRpnError

                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(Postfix.do_operation(token.value,num2,num1))
            else:
                # something wrong
                raise InvalidRpnError
        
        if stack[0] == float('inf'):
            raise ValueError('Number calculcted is too large to compute.')

        if len(stack) != 1:
            raise InvalidRpnError


    """
    parameter: a list of tokens initiated with class tokenizer
    returns: a decimal with the evaluation of an rpn notations

    just a small algorithim to evaluate an rpn

    """ 

    def evaluate_expression(self):

        stack = []

        for token in self.get_tokens():
            if token.type == Types.UNKNOWN:
                raise InvalidCharacterError(token.value)

            elif token.type == Types.NUMBER :
                stack.append(token.value)
            elif token.type == Types.OPERATOR:
                if len(stack)<2:
                    raise InvalidRpnError

                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(Postfix.do_operation(token.value,num2,num1))
            else:
                # something wrong
                raise InvalidRpnError
        
        if stack[0] == float('inf'):
            raise ValueError('Number calculcted is too large to compute.')

        return stack[0]


    @staticmethod
    def evaluate_expression_tokens(tokens):

        stack = []

        for token in tokens:
            if token.type == Types.NUMBER :
                stack.append(token.value)
            elif token.type == Types.OPERATOR:
                if len(stack)<2:
                    raise InvalidRpnError

                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(Postfix.do_operation(token.value,num2,num1))
            else:
                # something wrong
                raise InvalidRpnError
        
        if stack[0] == float('inf'):
            raise ValueError('Number calculcted is too large to compute.')

        return stack[0]       

    def __str__(self):

        try:
            res = self.evaluate_expression()
            return (f'[✓] The value of the expression is : {res} ')
        except InvalidCharacterError as e:
            return (f"[✕] Invalid Character '{e}' found in expression.")
        except InvalidRpnError:
            return (f'[✕] The Expression entererd is an invalid rpn.')
        except ZeroDivisionError:
            return ("[✕] The expression attempts to divide by zero.")
        except ValueError as e:
            return (e)

    def __eq__(self, other):
        if self.evaluate_expression()== other.evaluate_expression():
            return "both expressions are equal"
        else:
            return "expressions are not equal"

