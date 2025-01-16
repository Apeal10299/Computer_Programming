#Modify the "Times Table" again so that the user still enters the number of the table, but if this number is negative the table is printed backwards. 
# So entering "-7" would produce the Seven Times Table starting at "12 times" down to "0 times".


i = int(input("Enter a number for the Times Table: "))
if i < 0:
    for count in range(12, -1, -1):
        print(f"{count} * {i} = {count * i}")
else:
    for count in range(13):
        print(f"{count} * {i} = {count * i}")
