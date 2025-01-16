#Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion.
# Test both functions. 
# (Google will find you the formulae).

def centi_fah(centi):
    return (centi * (9/5)) + 32
    
def fah_centi(fah):
    return (fah - 32)*(5/9)

def main():
    choice=input("Choose one option (1. For Centigrade to Fahrenheit and 2. For Fahrenheit to Centigrade): ")
    
    if choice == "1":
        centi=float(input("Enter the centigrade: "))
        c_f = centi_fah(centi)
        print(f"{centi}°C is equivalent to {c_f}°F")

    elif choice == "2":
        fah=float(input("Enter the Fahrenheit: "))
        f_c = fah_centi(fah)
        print(f"{fah}°F is equivalent to {f_c:.2f}°C")

    else:
        print("Invalid Choice")
main()
