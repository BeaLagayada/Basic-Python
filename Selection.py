n=0
lst = [26,87,0,387,278,902,45]

print("List: ",lst)

for i in range(0, len(lst)):
    minIndex = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[minIndex]:
            minIndex = j
            n += 1

    lst[i], lst[minIndex] = lst[minIndex], lst[i]
    print(lst)

print("\nNumber of Steps: ", n)
print("Sorted List: ",list)



