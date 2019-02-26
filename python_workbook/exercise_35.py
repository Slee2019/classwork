years = float(input("Enter the amount of human years: "))
if years <= 2:
    dog_years = (years * 10.5)
    print(f"The amount of dog years is {dog_years}.")
elif years > 2:
    dog_years = (((years - 2) * 4) + (2 * 10.5))
    print(f"The amount of dog years is {dog_years}.")

