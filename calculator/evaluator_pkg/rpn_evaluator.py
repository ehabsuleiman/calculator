
import operator
from calculator.evaluator_pkg.postfix import InvalidCharacterError, InvalidRpnError
from calculator.utils import Types


"""
parameter: an operation to do,first number, second number
returns: a decimal with the evaluation of the operation

""" 
def do_operation(operation,num1,num2):
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        return InvalidCharacterError

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
    else:
        #operation not supported
        print('operation {operation} is not supported ')
        return 


"""
parameter: a list of tokens initiated with class tokenizer
returns: a decimal with the evaluation of an rpn notations

just a small algorithim to evaluate an rpn

""" 

def evaluate_postfix(tokens):

    stack = []

    for token in tokens:
        if token.type == Types.NUMBER :
            stack.append(token.value)
        elif token.type == Types.OPERATOR:
            if len(stack)<2:
                raise InvalidRpnError

            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(do_operation(token.value,num2,num1))
        else:
            # something wrong
            raise InvalidRpnError
    
    if stack[0] == float('inf'):
        raise ValueError('Number calculcted is too large to compute.')

    return stack[0]