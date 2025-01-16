#1.Modify your greeting program so that if the user does not enter a name (i.e. they just press enter),the program responds "Hello, Stranger!". 
# Otherwise it should print a greeting with their name as before.

my_name=input("Hello, What is your name? ")
if my_name=="":
    print("Hello Stranger!")
else:
    print(f"Hello, {my_name}. Good to meet you! ")
    