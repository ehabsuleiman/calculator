from enum import Enum
import re
from  calculator.token_pkg.token_class import Token
from calculator.utils import is_num,is_parentheses,is_operator,sanitize_string,Types


#enum to avoid errors
class Notaions(Enum):
    INFIX = 'INFIX'
    POSTFIX = 'POSTFIX'

"""
Tokenizer class takes in an expression and can spit out with a list of token class

""" 

class Tokenizer:
    def __init__(self,exp,notation = Notaions.INFIX):
        self.expression = exp
        self.notation = notation


    #uses below function as a property for ease
    @property
    def tokens(self):
        return self.tokenize_expression()



    """
    paremeter:takes an expression, takes in what no
    returns: a list of character with the class token

    """ 

    def tokenize_expression(self):
        tokens = []
        if self.notation == Notaions.INFIX:
            tokens = self.split_infix_expression(self.expression)
        elif self.notation == Notaions.POSTFIX:
            tokens = self.split_postfix_expression(self.expression)
        else:
            print("Notation not supported yet")

        return Tokenizer.construct_token_array(tokens)


    
    """
    paremeter:takes a list of characters
    returns: a list of character with the class token

    """ 
    @staticmethod
    def construct_token_array(tokens_expression):
    
        tokens = []

        for token in tokens_expression:
            if is_operator(token):
                tokens.append(Token(Types.OPERATOR,token))
            elif is_num(token):
                tokens.append(Token(Types.NUMBER,token))
            elif token == '(':
                tokens.append(Token(Types.LEFT_PAREN,token))
            elif token == ')':
                tokens.append(Token(Types.RIGHT_PAREN,token))
            else:
                tokens.append(Token(Types.UNKNOWN,token))

        return tokens


    #splits am array of postfix expression
    @staticmethod
    def split_postfix_expression(exp):

        #finds operators,deciamals,numbers
        res = re.findall(r'[0-9\.]+|[*/+-]', exp)

        n = len(res)

        #case of first number being negative 
        if n>1 and res[0]== '-':
            res[1] = '-' + res[1]
            res.pop(0)


        return res


    #splits the array based of infix expression
    @staticmethod
    def split_infix_expression(exp):

        #remove whitespace
        exp = sanitize_string(exp)

        #finds operators,deciamals,numbers
        res = re.findall(r'[0-9\.]+|[^0-9\  .]|[()^*/+-]', exp)

        n = len(res)


        #case of first number being negative 
        if n>1 and res[0]== '-':
            res[1] = '-' + res[1]
            res.pop(0)

        n =len(res)


        #mimimum of 3 length to combine negatives
        if n>3:
            for i in range(n-2):
                # handles case of a negative number right after a left parentheses
                if res[i]=='(' and res[i+1] == '-' and is_num(res[i+2]):
                    res[i+2] = '-' + res[i+2]
                    res.pop(i+1)
                # handles the case of operation and negative right after
                if(is_operator(res[i]) and res[i+1] == '-' and is_num(res[i+2]) ):
                    res[i+2] = '-' + res[i+2]
                    res.pop(i+1)

        return res