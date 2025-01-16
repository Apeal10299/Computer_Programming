#Modify the previous program so that it can process any number of values. 
# The input terminates when the user just pressed "Enter" at the prompt rather than entering a value.

def user_temperatures():
    temperatures = []
    while True:
        try:
            temperature = input("Enter a temperature (or press Enter to finish): ")
            if temperature == "":
                break
            temperatures.append(float(temperature))
        except ValueError:
            print("Please enter a valid number.")
    return temperatures

def calculation_part(temperatures):
    if temperatures:
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        return max_temp, min_temp, mean_temp
    else:
        return None, None, None

temperatures = user_temperatures()
if temperatures:
    max_temp, min_temp, mean_temp = calculation_part(temperatures)
    print("Maximum temperature: {:.2f}°C".format(max_temp))
    print("Minimum temperature: {:.2f}°C".format(min_temp))
    print("Mean temperature: {:.2f}°C".format(mean_temp))
else:
    print("No temperatures were entered.")

