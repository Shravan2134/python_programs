import time

# timestamp = time.strftime("%H:%M:%S", time.localtime())

def greet(name):
    timestamp = time.strftime("%H", time.localtime())
    if 5 <= int(timestamp) < 12:
        greeting = "Good morning"
    elif 12 <= int(timestamp) < 17:
        greeting = "Good afternoon"
    elif 17 <= int(timestamp) < 21:
        greeting = "Good evening"
    else:
        greeting = "Good night"
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    print("Thank you for using the greeting program!")
    print("Goodbye!")

