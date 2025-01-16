#Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2). 
# Hint: This is in many ways a trick question. Think!

def into_binary(n):
    return bin(n)[2:]
print(into_binary(5)) 
