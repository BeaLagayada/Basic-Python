t1= tuple ([2 * x for x in range(1,5)])
print(t1)

t2= tuple ("abac")
print(t2)

t3 = tuple([1,2,3,4,5,6,1])
print(t3)

number = float(input("Enter a Tuple: "))
text = input("Enter a string tuple: ")

t4 = (number, text)
print(t4)

print("length: ", len(t3))
print("max: ", max(t1))
print("min: ", min(t3))
print("sum: ", sum(t3))
print("first element: ", t3[0])

sum = t3 + t1
print(sum)

t0 = 2 * t1
print(t0)

print("print 2: ", 2 in t3)

lst = list(t3)
lst.sort()
t5 = tuple(lst)
t6 = tuple(lst)

print(t6 == t5)
print(t3[-1])

for v in t3:
    print(v, end= ' ')
print()
