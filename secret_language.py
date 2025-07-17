import random
import string

def generate_random_string(length=3):
    characters = "abcdefghijklmnopqrstuvwxyz"
    if len(characters) < length:
        raise ValueError("Character pool must be at least as long as the desired string length.")
    return ''.join(random.choices(characters, k=length))


def Secret_Coding(message):
    list = message.split(' ')
    new_word = ""
    Coded_message = ""
    new = ""
    # prefix = ''.join(random.choices(string.ascii_letters, k=3))
    # suffix = ''.join(random.choices(string.ascii_letters, k=3))
    prefix = ''.join(generate_random_string())
    suffix = ''.join(generate_random_string())
    for i in list:
        if len(i) >= 3:
            new_word = i + i[0]
            new_word = new_word[1:]
            new_word = prefix + new_word + suffix
            Coded_message += " " + new_word
        else:
            new = i[::-1]
            Coded_message = " " + new

    return Coded_message
            

def Secret_Decoding(str):
    list = str.split(' ')
    new_word = ""
    Decoded_message = ""
    for i in list:
        if len(i) < 3:
            correct_word = i[::-1]
            
        else:
            new_word = i[3:-3]
            correct_word = new_word[-1] + new_word[:-1]
        Decoded_message += " " + correct_word
    return Decoded_message
    
    


print(Secret_Coding("Hi Shravan How Are You"))
print(Secret_Decoding("iH juyhravanSwfl juyowHwfl juyreAwfl juyouYwfl"))
       
