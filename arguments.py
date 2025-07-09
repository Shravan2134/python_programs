## required arguments

## the required arguments are the varibles which are required to run a function and they are required compulsory

def sum(a,b):
    return a + b

print(sum(5,6)) #--> here 5 and 6 are required arguments

# default arguments

def multiply(x=5, n=11): # Here are the default arguments 
    for i in range(1,n):
        print(f"{x} * {i} =", x*1)
    print("thank you for using function")


print(multiply())  # if we call any function with default arguments without declaring argument values it will take default value of arguments

# key word arguments 

def details(a,b):
    print(f" my name is {a} and my age is {b}")


print(details(b="21", a="shravan"))  #--> use case of keyword arguments we can pass without followed order while declaring the arguments



# varible length arguments

def mean(*numbers): #--> declaration of variable length arguments (*x)
    sum = 0
    l = len(numbers)
    print(numbers)
    for i in numbers:
        sum += i
    print(f"The mean of the Numbers is",(sum)/l)

print(mean(12,31,1,2))    #--> while using variable length arguments we can use number of arguments while calling an function it will consider it as tuple
