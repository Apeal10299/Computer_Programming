#3. Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.

password_1 = input("Enter your new password: ")

if len(password_1) < 8 or len(password_1) > 12:
    print("Error: Password must be between 8 and 12 characters long. Please try again.")
else:
    password_2 = input("Re_enter your new password: ")

    if password_1==password_2:
        print("Password Set")
    else:
        print("Error: Password do not match. Please try again..")