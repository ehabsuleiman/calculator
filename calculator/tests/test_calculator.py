import unittest
from calculator.notations import InvalidCharacterError,InvalidOperationsError,InvalidParenthesesError,InvalidRpnError
from calculator.calculator_mod import evaluate_infix_expression,evaluate_postfix_expression


#using python library unittest to test
class TestCalc(unittest.TestCase):


    #some expressions that need only have one operator in succesion
    def test_one_operator(self):
        self.assertEqual(evaluate_infix_expression('4+     4'),8)
        self.assertEqual(evaluate_infix_expression('5  +   4*50/50'),9)
        self.assertEqual(evaluate_infix_expression('5-   5  -5'),-5)

    #some expressions that need  have multiple operator in succesion
    def test_multiple_operators(self):
        self.assertEqual(evaluate_infix_expression('4*-4'),-16)
        self.assertEqual(evaluate_infix_expression('-   5+   -5'),-10)
        self.assertEqual(evaluate_infix_expression('10   *  -5-6-  80'),-136)
        
    def test_decimal_values(self):
        self.assertEqual(evaluate_infix_expression('-.32       /.5'),-0.64)
        self.assertEqual(evaluate_infix_expression('1/5'),.2)

    def test_parentheses(self):
        self.assertEqual(evaluate_infix_expression('(((((-0.5+1)))))'),.5)
        self.assertEqual(evaluate_infix_expression('(4*4)+(4/4)'),17)


    #any big or complicated expressions
    def test_complex_expressions(self):
        self.assertEqual(evaluate_infix_expression('(5*5-(3-1))*(4--4--4+20)*(23*4-(10/2))'),64032)
        


    '''
    evaluate_infix_expreession will raise exceptions if the expression is invalid
    here we assert these exceptions are raised correctly
    
    '''

    def test_invalid_character_exception(self):
        self.assertRaises(InvalidCharacterError,evaluate_infix_expression,'4*a')
        self.assertRaises(InvalidCharacterError,evaluate_infix_expression,'4.&^&^&3434')

    def test_division_by_zero_exception(self):
        self.assertRaises(ZeroDivisionError,evaluate_infix_expression,'4/0')
        self.assertRaises(ZeroDivisionError,evaluate_infix_expression,'4/ (4-4)')

    def test_invalid_operation_exception(self):
        self.assertRaises(InvalidOperationsError,evaluate_infix_expression,'4**4')
        self.assertRaises(InvalidOperationsError,evaluate_infix_expression,'4*--4')        

    def test_invalid_parentheses_exception(self):
        self.assertRaises(InvalidParenthesesError,evaluate_infix_expression,'(3*4))')
        self.assertRaises(InvalidParenthesesError,evaluate_infix_expression,'(4*((4-2)')      




    #testing rpn functionalities also shows the modularity of the implementation
    def test_rpn_evaluate(self):
        self.assertEqual(evaluate_postfix_expression('3 5 6 + *'),33)
    
    def test_rpn_exceptions(self):
        self.assertRaises(InvalidRpnError,evaluate_postfix_expression,'5 + 5')      
        self.assertRaises(ZeroDivisionError,evaluate_postfix_expression,'5 0 /')      


if __name__ == '__main__':
    unittest.main()