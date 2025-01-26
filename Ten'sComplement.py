# Assigning a variable and Prompt the user to input a decimal number
num = int(input("Enter a decimal number: "))

# Calculating the ten's complement
tens_complement = 10 ** len(str(num)) - num

# Display the result
print("The Ten's Complement of", num, "is: ", tens_complement)

while True:
    num = int(input("Please enter 1 if you wish to continue or 0 to exit: "))

    if num == 1:
        num = int(input("Enter a decimal number: "))
        tens_complement = 10 ** len(str(num)) - num
        print("The Ten's Complement of", num, "is: ", tens_complement)
    else:
        print("Thank you for using!")
        break

