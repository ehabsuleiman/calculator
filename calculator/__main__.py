from calculator.calculator_mod import evaluate_infx_expression_with_feedback
from enum import Enum
import re

VALIDWORDS = ["CALCULATE","EVALUATE","EVAL","EXECUTE"]


#enum to avoid errors
class Methods(Enum):
    TEXT = '1'
    FILE = '2'
    END = '3'

            
def eval_expression(expression):
    try:

        #use calculator class to evaluate the expression
        res = re.findall('["][^"]+["]',expression)[0].replace('"','')
        res = evaluate_infx_expression_with_feedback(res)
        return res
    except OverflowError:
        print('\n[WARNING] Expression entered caused an overflow. \n')
    except SyntaxError:
        print('\n[WARNING] Expression entered caused a syntax error. \n')

        

#validated if input by user is valid
def is_valid_input(input):
    
    #validate if expression is a word then and input wrapped in quatation marks
    if not re.match('^\w+\s+["][^"]+["]$', input):
        return False

    #the word used
    word = re.findall('\w+',input)[0]

    #check if the word is valid
    if not word.upper() in VALIDWORDS:
        return False
    
    return True
        

if __name__ == '__main__':
    
    #loop till user inputs 3 to end the program
    while True:

        #ask user how he wantes to input expression
        print("\nPlease enter one of the following options to input you expression:\n")
        print("(1). A Text: Enter your expression manually.\n")
        print("(2). A File: Inputs you expression from expression.txt from this current directory.\n")
        print("(3). End Program: Terminates execution of the program.\n")

        method = input()

        if method == Methods.TEXT.value:
            user_input = input('\n[INFO] Please enter the expression in the format --> Calculate "Expression here inside quatations" : ')
        elif method == Methods.FILE.value:
            try:

                #default here is expression.txt consider changeing it to ask user input for file name
                f = open("expression.txt", "r")
            except (FileNotFoundError) as e:
                print('\n[WARNING]  The expression.txt file is not found in the directory. Please add it to your directory before executing.\n')
                continue
            user_input = f.read()
          
        elif method == method == Methods.END.value:
            exit(0)
        else:
            print("\n[INFO] Input did not match any of the options.\n")
            continue

        if user_input == '':
            print('\n[INFO] The input you entered is currently empty. \n ')
            continue
        
        if not is_valid_input(user_input):
            print('\n[WARNING] Expression entered is invalid, Please enter the expression in the format {Calculate Expression}. \n')
        else:
            output = eval_expression(user_input)
            print(f'\n{output} \n')


            
        

    
        