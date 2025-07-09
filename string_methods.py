## rstrip method
# The rstrip() method returns a copy of the string with trailing whitespace removed.

s = "   Hello, World!   "
striped = s.rstrip()
print(striped)


filename = "example.txt"
filename_without_extension = filename.rstrip(".txt")
print(f"Filename without extension: {filename_without_extension}")


# replace method
# The replace() method returns a copy of the string with all occurrences of a substring replaced by

text = "payment failed"
new_text = text.replace("failed", "successful")
print(new_text)

## split method used for separating strings into a list using the specified separator
# The split() method returns a list of substrings.

user_details = "Name: John Doe, Age: 30, Location: New York"
new = user_details.split(", ")
print(new)

# Different methods of case changing methods as defined below

name = "shravan"
print(name.capitalize())  # Capitalizes the first letter of the string
print(name.upper())       # Converts the entire string to uppercase
print(name.lower())       # Converts the entire string to lowercase
print(name.title())       # Capitalizes the first letter of each word in the string     

# center method
# The center() method returns a new string of a specified length with the original string centered within

print("auth".center(10, '*')) 

message = "Done"
print(message.center(20, '-')) 


# count method
# The count() method returns the number of occurrences of a substring in the string.

email = "user@domain.com"
print(email.count("@"))  

log = "Error: Retry. Error: Timeout."
print(log.count("Error"))  

# find method
# The find() method returns the lowest index of the substring if found in the string, otherwise
# it returns -1.

data = "Bearer token123"
print(data.find("token")) 

phrase = "Hello world"
print(phrase.find("z"))  

# index method
# The index() method returns the lowest index of the substring if found in the string, otherwise

id = "abc123xyz"
print(id.index("123"))  

# isalnum method
# The isalnum() method returns True if all characters in the string are alphanumeric (letters and digits),
# otherwise it returns False. It does not consider underscores or special characters.

token = "abc123"
print(token.isalnum())  

username = "user_01"
print(username.isalnum())  
