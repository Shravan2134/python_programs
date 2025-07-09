a = input("enter first number: ")
b = input("enter second number: ")

operators = input("enter operator (+, -, *, /): ")

if operators == "+":
    result = float(a) + float(b)
    print("The addition of", a, "and", b, "is:", result)
elif operators == "-":
    result = float(a) - float(b)
    print("The subtraction of", a, "from", b, "is:", result)
elif operators == "*":
    result = float(a) * float(b)
    print("The multiplication of", a, "and", b, "is:", result)
elif operators == "/":
    if float(b) != 0:
        result = float(a) / float(b)
        print("The division of", a, "by", b, "is:", result)
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print("Thank you for using the calculator!")
print("Goodbye!")
