#Last week you wrote a program that processed a collection of temperature readings entered by the user and displayed the maximum, minimum, and mean. 
# Create a version of that program that takes the values from the command-line instead. 
# Be sure to handle the case where no arguments are provided!

import sys

def main():
    if len(sys.argv) < 2:
        print("No temperature readings provided. Please provide temperature values as command-line arguments.")
        return

    try:
        temperatures = [float(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Please provide valid numeric temperature readings.")
        return

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"Mean temperature: {mean_temp:.2f}")
main()