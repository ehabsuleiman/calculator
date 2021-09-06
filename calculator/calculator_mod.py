from calculator.token_pkg.tokenizer import Tokenizer,Notaions
from calculator.notations.infix import InvalidCharacterError, InvalidOperationsError, InvalidParenthesesError, InvalidExpressionError,InvalidRpnError,infix 
from calculator.notations.postfix  import postfix


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
    res = postfix(expression)
    return res.evaluate_expression()      
   
#evaluate_expression: returns a decimal evaluation of the expression
def evaluate_infix_expression(expression):
    res = infix(expression)
    return res.evaluate_expression()    

#evaluate_expression: returns a decimal evaluation of a infix expression with feedback
def evaluate_infx_expression_with_feedback(expression):

    try:
        res = infix(expression)
        return res.__str__
    except:
        return ('An error occured in evaluating expression')
#evaluate_expression: returns a decimal evaluation of a infix expression with feedback
def evaluate_postfix_expression_with_feedback(expression):

    try:
        res = postfix(expression)
        return res.__str__
    except:
        return ('An error occured in evaluating expression')
    
