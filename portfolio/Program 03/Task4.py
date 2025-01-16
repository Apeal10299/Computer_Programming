#Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus: 
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password_1 = input("Enter your new password: ")

if password_1 in BAD_PASSWORDS:
    print("Error: Password cannot be one of the following: ['password', 'letmein', 'sesame', 'hello', 'justinbieber']!")
elif len(password_1) < 8 or len(password_1) > 12:
    print("Error: Password must be between 8 and 12 characters long. Please try again.")
else:
    password_2 = input("Re-enter your new password: ")

    if password_1 == password_2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")
