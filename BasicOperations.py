import random

print("ELAGAYADA")
print("Calculating four basic operations (+,-,*,/)")

#generating random numbers
l = (random.randrange(1,99))

p = (random.randrange(1,99))

#calculating addition operation
answer = l + p
num = eval(input(f"\nWhat is  {l} + {p} ?" ))
print(f"{l} + {p} =", num)

#Checking answers
if answer == num:
     print("Your answer is correct!")
else:
     print("Your answer is incorrect!")

#generating random numbers
a = (random.randrange(1,99))

b = (random.randrange(1,99))

#Calculating subtraction operation
answer = a - b
num = eval(input(f"\nWhat is  {a} - {b} ?" ))
print(f"{a} - {b} =", num)

#Checking answers
if answer == num:
     print("Your answer is correct!")
else:
     print("Your answer is incorrect!")

#generating random numbers
y = (random.randrange(1,99))

z = (random.randrange(1,99))

#Calculating multiplication operation
answer = y * z
num = eval(input(f"\nWhat is  {y} * {z} ?" ))
print(f"{y} * {z} =", num)

#Checking answers
if answer == num:
     print("Your answer is correct!")
else:
     print("Your answer is incorrect!")

#generating random numbers
f = (random.randrange(1,99))

g = (random.randrange(1,99))

#Calculating division operation
answer = f / g
num = eval(input(f"\nWhat is  {f} / {g} ?" ))
print(f"{f} / {g} =", num)

#Checking answers
if answer == num:
     print("Your answer is correct!")
else:
     print("Your answer is incorrect!")
