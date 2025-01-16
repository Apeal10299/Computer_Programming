#7. Modify your "Times Table" program so that the user enters the number of the table they require. 
# This number should be between 0 and 12 inclusive.

i=int(input("Enter your number for the Times Table: "))
for count in range(0,13):
    print(f"{count} * {i} = {count*i}")