#2. Write a program that simulates the way in which a user might choose a password. 
# The program should prompt for a new password, and then prompt again. 
# If the two passwords entered are the same the program should say "Password Set" or similar, otherwise it should report an error.

password_1 = input("Enter your new password: ")
password_2 = input("Re_enter your new password: ")

if password_1==password_2:
    print("Password Set")
else:
    print("Error: Password do not match. Please try again..")