#Modify your program a final time so that it executes until the user successfully chooses a password. 
# That is, if the password chosen fails any of the checks, the program should return to asking for the password the first time.

while True:
   BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
   password_1 = input("Enter your new password: ")

   if password_1 in BAD_PASSWORDS:
     print("Password connot be ['password', 'letmein', 'sesame', 'hello', 'justinbieber']!")
     continue
   if len(password_1) < 8 or len(password_1) > 12:
       print("Error: Password must be between 8 and 12 characters long. Please try again.")
       continue
   password_2 = input("Re_enter your new password: ")

   if password_1 == password_2:
    print("Password Set")
    break
   else:
    print("Error: Password do not match. Please try again..")