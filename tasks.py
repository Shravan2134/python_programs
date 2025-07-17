from ast import literal_eval
import math

# def type_detector():
#     try:
#         example = literal_eval(input("Enter the data:"))
#         print(type(example))
#     except Exception as e:
#         print("Error: Invalid Input", e)


# type_detector()

class NumeratorZeroError(Exception):
    pass

class ValidTypeError(Exception):
    pass

class DenominatorZeroError(Exception):
    pass

class NumbersZeroError(Exception):
    pass

class ZeroMultiplicationError(Exception):
    pass

def Dynamic_calculator():
    try:
        a = eval(input("enter the first number:"))
        b = eval(input("enter the second number:"))
        if type(a) == "int":
            raise ValidTypeError("Type of values should be integer")
        else:
            operator = input("select the operator to perfrom your operation [+,-,/,*]")
            if operator == "+":
                res = a + b
            elif operator == "-":
                res = a - b
            elif operator == "/":
                if a == 0:
                    raise NumeratorZeroError("Numerator cannot be zero")
                elif b == 0:
                    raise DenominatorZeroError("Denominator cannot be zero")
                elif a == b == 0:
                    raise NumbersZeroError("Zeros cannot be divided")
                else:
                    res = a/b
            elif operator == "*":
                if a == 0 or b == 0:
                    raise ZeroMultiplicationError("Number should not be multiplied by 0")
                else:
                    res = a*b
            else:
                print(f"{operator} is not a valid operator please select an valid operator")
        return res
    
    except NumeratorZeroError as e:
        print("Error", e)

    except DenominatorZeroError as e:
        print("Error", e)

    except NumbersZeroError as e:
        print("Error", e)

    except ZeroMultiplicationError as e:
        print("Error", e)

    except ValidTypeError as e:
        print("Error", e)

    finally:
        print("The program executed successfully")
        

        
        
    
result = Dynamic_calculator()

if result is not None:
    print("Final Result", result)



   