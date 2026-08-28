# working with numbers
from itertools import product

from pyscript import display, document

import random
def greetings(e): # initialize function
    document.getElementById('result').innerHTML = " " #clear the previous result
    username = document.getElementById('user_input').value # getting the date from a textbox
    display(f'{random.choice(["Welcome back", "Hello again", "It\'s all yours", "Ready to calculate?", "Ready to find out what 1+1 is?"])}, {username}.', target='result') #I wanted to make the greetings different so I searched up online and used random.choice.


def adding_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number # This adds the two numbers together thus giving the sum of the two numbers

    display(f'The sum of {first_number} and {second_number} is {sum}', target='result')

def subtracting_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number # This subtracts the two numbers, giving the difference

    display(f'The difference of {first_number} and {second_number} is {difference}', target='result')

def multiplying_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number * second_number # This multiplies the two numbers giving the product.

    display(f'The product of {first_number} and {second_number} is {product}', target='result')    

def dividing_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number / second_number # this divides the two numbers giving the quotient.

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='result')

def floordiv_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number // second_number # this divides the two numbers giving the quotient but rounds down to the nearest whole number.

    display(f'The quotient of {first_number} and {second_number} is {quotient}', target='result')

def modulus_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number % second_number # this divides the two numbers giving the remainder of the division.

    display(f'The remainder of {first_number} and {second_number} is {quotient}', target='result')    

def exponentation_numbers(e):
    document.getElementById('result').innerHTML = " " #clear the previous result
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number ** second_number # this raises the first number to the power of the second number. It is 

    display(f'The result of {first_number} raised to the power of {second_number} is {quotient}', target='result')                     
