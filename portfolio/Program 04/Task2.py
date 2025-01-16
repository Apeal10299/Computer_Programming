#Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string. 
# Test the function with a short program.

def single_string():
    s = input("Enter a string: ")
    uppercase = sum(1 for c in s if c.isupper())
    lowercase = sum(1 for c in s if c.islower())
    return uppercase, lowercase
print(single_string())