cents = int(input("How many cents do you have?: "))
toonies = cents // 200
loonies = (cents % 200) // 100
quarters = ((cents % 200) % 100) // 25
dimes = (((cents % 200) % 100) % 25) // 10
nickels = ((((cents % 200) % 100) % 25) % 10) // 5
pennies = (((((cents % 200) % 100) % 25) % 10) % 5)
print(f"{cents} is: ")
print(f"{cents} cents is: ")
print(f"{toonies} - toonies")
print(f"{loonies} - loonies")
print(f"{quarters} - quarters")
print(f"{dimes} - dimes")
print(f"{nickels} - nickels")
print(f"{pennies} - pennies")