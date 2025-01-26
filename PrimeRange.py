#introduction
print("CS112: COMPUTER PROGRAMMING 1 - PRE-FINAL EXAM")
print("Created by: Bea A. Lagayada")

#problem
print("\nProblem: Create a python program that displays all prime numbers within a range:")

#rules
print("\nRULES TO CONSIDER:")
print('[1] If number[start] is a negative number. The program will prompt a message: "Enter a non-negative number"')
print('[2] If number[end] is less than number[start]. The program will prompt a message: "Enter a number greather than number[start]"')
print('[3] If the user enter the number "0", the program will terminate.')

#user input
while True:
    start_range = int(input("\nEnter a number [start]: "))

    #terminate the program if the user enters 0
    if start_range == 0:
        print("Program Terminated.")
        break

    #check if the start_range is a non-negative number
    if start_range < 0:
        print("Enter a non-negative number.")
        continue

    end_range = int(input("Enter a number [end]: "))

    #check if the end_range is greater than the start_range
    if end_range <= start_range:
        print(f"Enter a number greater than {start_range}.")
        continue

    #display prime numbers
    print(f"Prime numbers between {start_range} and {end_range} are: ", end=" ")

    #formula in getting prime numbers
    for number in range(start_range, end_range + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number, end=" ")
    print()
