from calculator.token_pkg.tokenizer import Tokenizer,Notaions
from calculator.evaluator_pkg.postfix  import InvalidCharacterError, InvalidOperationsError, InvalidParenthesesError, InvalidExpressionError,InvalidRpnError,ConvertToPostfix 
from calculator.evaluator_pkg.rpn_evaluator  import evaluate_postfix


"""
module Calculator has the following main methods:

    evaluate_infix_expression: takes in an expression returns a decimal evaluation of the expression
    evaluate_infx_expression_with_feedback: takes in an expression returns a decimal evaluation of the expression and returns come feedback if value not found
    calculate_postfix: takes in a expression and returns the postfix of the exprssion
    evaluate_rpn_expression: takes in an rpn expression and returns a decimal evaluation of it
    evaluate_rpn_tokens: takes in an rpn tokens and returns a decimal evaluation of it

""" 


#evaluate_rpn: returns the evaluation of an rpn from postfix notation that is initizlaized with tokens
def evaluate_rpn_tokens(postfix_tokens):
    res = evaluate_postfix(postfix_tokens)
    return res

#evaluate_rpn: returns the evaluation of an rpn from postfix notation 
def evaluate_rpn_expression(postfix):
    tokens = Tokenizer(postfix,Notaions.POSTFIX).tokens
    res = evaluate_postfix(tokens)
    return res      
   
#evaluate_expression: returns a decimal evaluation of the expression
def evaluate_infix_expression(expression):
    res = ConvertToPostfix(expression) 
    res = evaluate_postfix(res.infix_to_postfix())
    return res

#evaluate_expression: returns a decimal evaluation of a infix expression with feedback
def evaluate_infx_expression_with_feedback(expression):

    try:
        res = evaluate_rpn_tokens(calculate_postfix(expression))
        return (f'[✓] The value of the expression is : {res} ')
    except InvalidCharacterError as e:
        return (f"[✕] Invalid Character '{e}' found in expression.")
    except InvalidExpressionError:
        return (f'[✕] The Expression entererd is invalid.')
    except InvalidOperationsError:
        return ("[✕] Invalid order of opertaions.")
    except InvalidParenthesesError:
        return ("[✕] Parantheses in expression are mismatched.")
    except ZeroDivisionError:
        return ("[✕] The expression attempts to divide by zero.")
    except ValueError as e:
        return (e)

    

#returns a list initilized with token class from an expression string
def calculate_postfix(expression):
    res = ConvertToPostfix(expression) 
    return res.infix_to_postfix()
