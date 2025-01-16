#Functions are often used to validate input. 
# Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise. 
# Write a short program to test the function.

def help():
    count=int(input("Enter any parameter: "))
    if count in range(0,101):
        print("True")
    else:
        print("False")
help()