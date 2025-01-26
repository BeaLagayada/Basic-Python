# prompt the user to enter a year
year = int(input("Please Enter a Year: "))

# Calculate and determine the Chinese zodiac sign based on the year
if year % 12 == 0:
    Zodiac_sign = "Monkey"
elif year % 12 == 1:
    Zodiac_sign = "Rooster"
elif year % 12 == 2:
    Zodiac_sign = "Dog"
elif year % 12 == 3:
    Zodiac_sign = "Pig"
elif year % 12 == 4:
    Zodiac_sign = "Rat"
elif year % 12 == 5:
    Zodiac_sign = "Ox"
elif year % 12 == 6:
    Zodiac_sign = "Tiger"
elif year % 12 == 7:
    Zodiac_sign = "Rabbit"
elif year % 12 == 8:
    Zodiac_sign = "Dragon"
elif year % 12 == 9:
    Zodiac_sign = "Snake"
elif year % 12 == 10:
    Zodiac_sign = "Horse"
else:
    Zodiac_sign = "Sheep"

# Display the output
print("\nThe Chinese Zodiac sign for the year", year, "is", Zodiac_sign)
