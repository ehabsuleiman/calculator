import re
from enum import Enum


OPERATORS = ['/','*','+','-']
PARENTHESES = ['(',')']


#enum to avoid errors
class Types(Enum):
    NUMBER = 'NUMBER'
    OPERATOR = 'OPERATOR'
    PARENETHESES = 'PARENETHESES'
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    UNKNOWN = 'UNKNOWN'

def remove_brackets(str):
    return re.sub(r"[^()]+","",str)

#remove whitespace
def sanitize_string(str):
    return re.sub('\s+','',str)

def is_operator(str):
    return str in OPERATORS
    
def is_parentheses(str):
    return str in PARENTHESES

def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

