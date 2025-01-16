#Write a program that, when run from the command line, reports how many arguments were provided. 
#(Remember that the program name itself isnotan argument).
import sys
def main():
    num_arguments = len(sys.argv) - 1  
    print(f"Number of arguments provided: {num_arguments}")
main()
