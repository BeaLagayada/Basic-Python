# Number System
print("****************************")
print("| Number System Conversion |")
print("****************************")
print("By: Bea A. Lagayada & Jules Rafael J. Mag-isa")

# prompt the user to enter a number
user = eval(input("Enter a number: "))

# Options
print("\n**********************************************")
print("[1] Decimal Number to Binary Number")
print("[2] Decimal Number to Octal Number")
print("[3] Decimal Number to Hexadecimal Number")
print("**********************************************")

#prompt the user to enter an option
answer = eval(input(f"\nHow do you want to convert {user} ? Enter from [1-3]:"))

# Calculating the number systems
if answer >= 4:
    print("Invalid Option. Please try again.", answer)
elif answer == 1:
    print("\n**********************************************")
    print("Decimal", user, "Converted to Binary Number is", format(user, 'b'))
    print("**********************************************")
elif answer == 2:
    print("\n**********************************************")
    print("Decimal", user, "Converted to Binary Number is", format(user, 'o'))
    print("**********************************************")
else:
    print("\n**********************************************")
    print("Decimal", user, "Converted to Binary Number is", format(user, 'x'))
    print("**********************************************")
