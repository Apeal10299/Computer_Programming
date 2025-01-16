#Write a program that decrypts messages encoded as above.

def decrypt(encrypted_message, interval):
    # Decrypted message will hold only the characters at the interval positions
    decrypted_message = ''
    
    # Traverse the encrypted message and pick every `interval`-th character
    for i in range(0, len(encrypted_message), interval):
        decrypted_message += encrypted_message[i]
    
    return decrypted_message

# Example usage (you must know the interval used for encryption)
encrypted_message = "svmchspehyriwpnvrashydiwhtffppzpgicqusuefhklontkenljuqnemhzclfsiopcgte"  # Example encrypted message
interval_used = 4  # Interval used during encryption (this should be known)

decrypted_message = decrypt(encrypted_message, interval_used)
print(f"Decrypted message: {decrypted_message}")
