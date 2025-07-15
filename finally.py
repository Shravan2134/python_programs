# try:
#     l = [1, 2, 3, 4]
#     i = int(input("Enter an index: "))
#     print("Value at index", i, "is", l[i])
# except:
#     print("some error ocurred")
# finally:
#     print("i am finally block")


# def final_block():
#     try:
#         with open("test02.txt", "r") as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print("File not found. Please check the file path.")
#     finally:
#         print("Execution of the try-except block is complete.")
    

# final_block()

# def Valid_input_try():
#     count = 3
#     i = 1
#     while i <= 3:
#         try:
#             num = int(input("enter the number:"))
#             print("You entered a num", num)
#         except ValueError:
#             print("Invalid input! Please enter a valid integer.")
#             i += 1
#             count -= 1
#         finally:
#             print(f"Attempts left: {count}")
#             if count == 0:
#                 print("No attempts left. Exiting.")
#                 break
#             else:
#                 print("You can try again.")
#                 continue

# Valid_input_try()


# def validate_division():
#     try:
#         a = int(input("Enter the numerator: "))
#         b = int(input("Enter the denominator: "))
#         result = a / b
#         print(f"The result of {a} divided by {b} is {result}")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     finally:
#         print("Execution of the division operation is complete.")


# validate_division()

class NumeratorValidationError(Exception):
    pass

def Numerator_Validation():
       try:
           a = int(input("Enter the numerator: "))
           b = int(input("Enter the denominator: "))
           if a < 5:
               raise NumeratorValidationError("Numerator cannot be less than 5")
           else:
                result = a / b
                print(f"The result of {a} divided by {b} is {result}")
       except NumeratorValidationError as e:
              print("Error:", e)

       except ZeroDivisionError:
           print("Error: Division by zero is not allowed.")
       finally:
            print("Validation check complete")

Numerator_Validation()