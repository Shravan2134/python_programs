def division(a,b):
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        print(f"The result of {a} divided by {b} is {result}.")
        return result


class NumeratorZeroError(Exception):
    pass

def division():
    try:
        a = int(input("Enter the numerator: "))
        if a == 0:
            raise NumeratorZeroError("Numerator cannot be zero")
    
        
        b = int(input("Enter the denominator: "))
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: The denominator cannot be zero.")
    except ValueError:
        print("Error:" , e)
    except NumeratorZeroError as e:
        print("ERROR!" ,e)
    except Exception as e:
        print("Unexpected error:", e)

# Call the function to test
division()


class NumberRangeError(Exception):
    pass

class InputError(Exception):
    pass

def division():
    try:
        a = int(input("Enter the number:"))
        if a > 20:
            raise NumberRangeError("Range should not exceed 20")

        b = int(input("Enter the number:"))
        if b == 0:
            raise InputError("Input should not be zero")

        print("Result:", a / b)

    except NumberRangeError as e:
        print("Error:", e)
    except InputError as e:
        print("ERROR:", e)

division()


def File_Reader(filename):
    try:
        with open(filename, 'r') as file:
            print("first_line", file.readline())
    except FileNotFoundError:
        print("Error: File not Found")

print(File_Reader("test.txt"))


class StudentNotFoundError(Exception):
    pass
class EmptyNameError(Exception):
    pass

marks = {"alice":83, "shravan": 97, "venky": 90, "siri": 92}

def Marks_finder():
    try:
       name = input("enter the name of the student:")
       if name not in marks.keys() and name != "":
           raise StudentNotFoundError("Student details not Found")
       elif name == "":
           raise EmptyNameError("Name cannot be empty")
       else:
           print("Marks", marks[name])
    except StudentNotFoundError as e:
        print("Error!", e)
    except EmptyNameError as e:
        print("Error!", e)
        

print(Marks_finder())
        
        
class ConversionError(Exception):
    pass

def input_conversion():
    while True:
        try:
            entry = input("Enter the number:")
            if not entry.strip().isdigit():
                raise ConversionError("Input is not an valid input")
            number = int(entry)
        except ConversionError as e:
            print("Error", e)
            
        
        
        
input_conversion()
               
