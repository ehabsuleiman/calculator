import calculator
from calculator import InvalidCharacterError
from calculator.evaluator_pkg.postfix import InvalidOperationsError


res = calculator.evaluate_infx_expression_with_feedback('4+4+4+4')
print(res)

rpn = calculator.evaluate_rpn_expression('4 4 +')
print(f'The rpn expression value is {rpn}.')


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

