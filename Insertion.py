lst = [26,87,0,387,278,902,45]

n = 0

print("Unsorted List: ", lst)

for i in range(1, len(lst)):
    value = lst[i]

    j = i-1
    while j >= 0 and value < lst[j]:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = value
    print(lst)


print("\nNumber of Steps: ", n)
print("Sorted List: ")
print(lst)