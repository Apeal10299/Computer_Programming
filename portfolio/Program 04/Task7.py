#Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum, and mean of the values. 
# Hint: You should know there are built-in functions for max and min. If you hunt, you might also find one for the mean.

def user_temperatures():
    temperatures = []
    for i in range(6):
        temperature = float(input("Enter temperature {}: ".format(i + 1)))
        temperatures.append(temperature)
    return temperatures

def calculation_part(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    return max_temp, min_temp, mean_temp

temperatures = user_temperatures()
max_temp, min_temp, mean_temp = calculation_part(temperatures)
print("Maximum temperature: {:.2f}°C".format(max_temp))
print("Minimum temperature: {:.2f}°C".format(min_temp))
print("Mean temperature: {:.2f}°C".format(mean_temp))
