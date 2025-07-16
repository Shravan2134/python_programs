from ast import literal_eval
import math

def type_detector():
    try:
        example = literal_eval(input("Enter the data:"))
        print(type(example))
    except Exception as e:
        print("Error: Invalid Input", e)


# type_detector()

class NumeratorZeroError(Exception):
    pass

def Dynamic_calculator():
    try:
        a = int(input("enter the first number:"))
        b = int(input("enter the second number:"))
        operator = input("select the operator to perfrom your operation [+,-,/,*]")

        if operator == "+":


   