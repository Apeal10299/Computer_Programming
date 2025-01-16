#Write a program that takes a bunch of command-line arguments, and then prints out the shortest. 
#If there is more than one of the shortest length, any will do.
#Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''

import sys
def main():
    arguments = sys.argv[1:]
    if not arguments:
        print("No arguments provided.")
        return
    shortest_arg = sorted(arguments, key=len)[0]
    print(f"The shortest argument is: {shortest_arg}")
main()
