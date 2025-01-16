#Modify your "greetings" program so that the first letter of the name entered is always in uppercase with the rest in lowercase. 
# This should happen even if the user entered their name differently. 
# So if the user entered arthur, ARTHUR, or even arTHur the name should be displayed as Arthur.

def greeting():
    my_name=input("Hello, What is your name? ")
    my_name = my_name.capitalize()
    if my_name=="":
        print("Hello Stranger!")
    else:
        print(f"Hello, {my_name}. Good to meet you! ")
greeting() 