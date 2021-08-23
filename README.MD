# Calculator

Calculator is a module that evaluates postfix and infix notations and provided functions for you to use them and other util functions to validate the expression.


## Prerequisites
Make sure to use python 3 to run the program


## Installation 

1. Clone the repo
   ```sh
   git clone  https://github.com/ehabsuleiman/calculator.git
   ```
2. have an expression.txt with your expression inside the file inside the directory you are currently in
3. be in main directory and run 
   ```python
   python calculator/setup.py install --user
   ```

## Running Main
1. make sure you have installed the package
2. run this command on the main directory
   ```python
   python -m calculator
   ```


## Showcase of main

![Screenshot](https://github.com/ehabsuleiman/calculator/blob/main/images/screenshot.PNG)

## Testing(running unit test)
 be in main directory and run 
   ```python
   python -m unittest discover
   ```

## Usage

```python
import calculator

# returns (10)
calculator.evaluate_infix_expression('5+5')

# returns invalid character a
calculator.evaluate_infx_expression_with_feedback('5+a')

```
## License
MIT