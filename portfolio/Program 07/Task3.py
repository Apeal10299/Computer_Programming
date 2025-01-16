#Write a program that manages a list of countries and their capital cities. 
#It should prompt the user to enter the name of a country. 
#If the program already "knows" the name of the capital city, it should display it. 
#Otherwise it should ask the user to enter it. 
#This should carry on until the user terminates the program (how this happens is up to you). 
#Note: A good solution to this task will be able to cope with the country being entered variously as, for example, "Wales", "wales", "WALES" and so on.

def manage_capitals():
    country_capitals = {}

    while True:
        country = input("Enter a country (or type 'exit' to quit): ").strip()

        if country.lower() == 'exit':
            print("Exiting the program...")
            break

        country_lower = country.lower()

        if country_lower in country_capitals:
            print(f"The capital city of {country} is {country_capitals[country_lower]}.")
        else:
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
            country_capitals[country_lower] = capital
            print(f"Thank you! I've stored the capital of {country} as {capital}.")

manage_capitals()
