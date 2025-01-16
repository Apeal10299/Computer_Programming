#Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit. 
# The input should be a number followed by a letter C. 
# The output should be in the same format.

def celsius_to_fahrenheit(temp_c):

    if not temp_c.endswith("C"):
        raise ValueError("Input must end with 'C'.")
    
    try:
        celsius = float(temp_c[:-1])  # Extract the numeric part
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit:.2f}F"  # Format output with 2 decimal places
    except ValueError:
        raise ValueError("Invalid numeric input.")

# Example usage
def main():
    input_temp = input("Enter temperature in Celsius (e.g., 25C): ").strip()
    try:
        result = celsius_to_fahrenheit(input_temp)
        print(f"Equivalent Fahrenheit temperature: {result}")
    except ValueError as e:
        print(f"Error: {e}")

main()
