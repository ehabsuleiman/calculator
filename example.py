from calculator.notations.infix import Infix
import calculator
from calculator import InvalidCharacterError,InvalidOperationsError
from calculator import evaluate_infix_expression,evaluate_postfix_expression,Postfix,evaluate_expressions


res = calculator.evaluate_infix_expression('4+4+4%4')
print(res)

rpn = calculator.evaluate_postfix_expression('4 4 +')
print(f'The rpn expression value is {rpn}.')


result = evaluate_expressions('4+4','4 4 +','(43*434)','3*+4')
print(result)

try:
    res = calculator.evaluate_infix_expression('4+4+4+a')
    print(res)
except InvalidCharacterError as e:
    print(f'Invalid character {e} .')

try:
    res = calculator.evaluate_infix_expression('4++4')
    print(res)
except InvalidOperationsError:
    print(f'Invalid operations in expression.')

