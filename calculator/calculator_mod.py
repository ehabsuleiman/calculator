from calculator import notations
from calculator.token_pkg.tokenizer import Tokenizer,Notaions
from calculator.notations import InvalidCharacterError, InvalidOperationsError, InvalidParenthesesError, InvalidExpressionError,InvalidRpnError
from calculator.notations.infix import Infix 
from calculator.notations.postfix  import Postfix


"""
module Calculator has the following main methods:

    evaluate_infix_expression: takes in an expression returns a decimal evaluation of the expression
    evaluate_infx_expression_with_feedback: takes in an expression returns a decimal evaluation of the expression and returns come feedback if value not found
    calculate_postfix: takes in a expression and returns the postfix of the exprssion
    evaluate_rpn_expression: takes in an rpn expression and returns a decimal evaluation of it
    evaluate_rpn_tokens: takes in an rpn tokens and returns a decimal evaluation of it

""" 


#evaluate_rpn: returns the evaluation of an rpn from postfix notation 
def evaluate_postfix_expression(expression):
    res = Postfix(expression)
    return res.evaluate_expression()      
   
#evaluate_expression: returns a decimal evaluation of the expression
def evaluate_infix_expression(expression):
    res = Infix(expression)
    return res.evaluate_expression()


def evaluate_expression(expression):
    try:
        res= Infix(expression).evaluate_expression()
        return (f'The {expression} result is {res}')
    except:
        pass
    try:
        res= Postfix(expression).evaluate_expression()
        return (f'The expression: {expression} result is {res}')
    except:
        return (f'The expression: {expression} entered is not a valid one')

def evaluate_expressions(*expression):
    res = []
    for expression in expression:
        res.append(evaluate_expression(expression))
    return res


#evaluate_expression: returns a decimal evaluation of a infix expression with feedback
def evaluate_infx_expression_with_feedback(expression):

    try:
        res = Infix(expression)
        return res.__str__()
    except:
        return ('An error occured in evaluating expression')
        
#evaluate_expression: returns a decimal evaluation of a infix expression with feedback
def evaluate_postfix_expression_with_feedback(expression):

    try:
        res = Postfix(expression)
        return res.__str__()
    except:
        return ('An error occured in evaluating expression')
    
