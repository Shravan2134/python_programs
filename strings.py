word = "shravan"
l = len(word)//2

def create_string():
    if len(word) % 2 == 0:
        middle = word[l-1:l+1]
        print(word[0]+ middle + word[4])
    else:
        middle = word[l]
        print(word[0] + middle + word[4])     
    
def count_vowels():
    vowels = "aeiou"
    count = 0
    main = len(word)
    for char in word:
        if char.lower() in vowels:
            count = count + 1
    print("The number of vowels in the word is:", count)
    print("The number of consonants in the word is:", main - count)

def check_anagram():
    word2 = "anavars"
    if sorted(word) == sorted(word2):
        print(f"{word} and {word2} are anagrams.")
    else:
        print(f"{word} and {word2} are not anagrams.")  

def check_anagrams():
    word3 = "killers"
    if len(word) != len(word3):
        print(f"{word} and {word3} are not anagrams.")
    else:
        for char in word.lower():
            if char not in word3.lower():
                print(f"{word} and {word3} are not anagrams.")
                return
        print(f"{word} and {word3} are anagrams.")

def string_validator():
    string = "My name is Shravan! I love Python3."
    white_space = 0
    digits = 0
    special = 0
    vowel_count = 0
    vowels = "aeiouAEIOU"
    special_characters = "!@#$%^&*()_+-=[]{}|;':\",.<>?/"
    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
        elif char.isdigit():
            digits += 1
        elif char in special_characters:
            special += 1
        elif char.isspace():
            white_space += 1        
    print("vowels:", vowel_count)
    print("digits:", digits)
    print("special characters:", special)
    print("white_spaces:", white_space)
    print("consonants:", len(string) - (vowel_count + digits + special + white_space))



def camel_case_TO_snake_case(str):
    # camel_case_string = "camelCaseString"
    snake_case_string = ""
    for char in str:
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            snake_case_string += char
    print("Camel case to snake case:", snake_case_string)


def Doc_str():
    """
    This function demonstrates the use of docstrings in Python.
    It prints a message indicating that it is a docstring example.
    """
    return "This is an example of a docstring in Python."


print(Doc_str())



    