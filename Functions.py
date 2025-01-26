def sum(first_number, second_number, third_number):

    sum = first_number + second_number + third_number

    if first_number == second_number == third_number:
        result = first_number * second_number * third_number
    elif first_number == second_number:
        result = (first_number * second_number) + third_number
    elif first_number == third_number:
        result = (first_number * third_number) + second_number
    elif second_number == third_number:
        result = (second_number * third_number) + first_number
    else:
        result = sum

    return result

first_number = eval(input("Enter first number: "))
second_number = eval(input("Enter second number: "))
third_number = eval(input("Enter third number: "))

result = sum(first_number,second_number, third_number)
print(f"Result is {result}")



