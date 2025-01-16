#Another way to hide a message is to include the letters that make it up within seemingly random text. 
#The letters of the message might be every fifth character, for example. 
#Write and test a function that does such encryption. 
#It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. 
#The function should return the encrypted message and the interval used. 
#For example, if the message is "send cheese", the random interval is 2, and for clarity the random letters are not random: send cheese 
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye



import random
import string

def encrypt(input_message):
    random_interval = random.randint(2, 20)
    result_message = ''
    for index, character in enumerate(input_message):
        result_message += character
        if index < len(input_message) - 1:
            result_message += ''.join(random.choices(string.ascii_lowercase, k=random_interval - 1))
    return result_message, random_interval

# Example usage
original_message = "send cheese"
encrypted_output, interval_used = encrypt(original_message)

print(f"Original message: {original_message}")
print(f"Encrypted message: {encrypted_output}")
print(f"Interval used: {interval_used}")
