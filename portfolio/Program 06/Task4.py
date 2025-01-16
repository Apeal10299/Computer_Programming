#Computers are commonly used in encryption.
# A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string. 
#Write, and test, a function that takes a string containing a message and "encrypts" it in this way.

def encrypt_message(message):
    return ''.join(message.replace(" ", "")[::-1])

user_message = input("Enter a message: ")
encrypted_message = encrypt_message(user_message)

print(f"Original Message: {user_message}")
print(f"Encrypted Message: {encrypted_message}")
