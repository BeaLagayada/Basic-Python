lst = [26,87,0,387,278,902,45]

n = 0
print("Unsorted:",lst)

for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            n+=1
            print(lst)

print("\nNumber of Steps: ",n)
print("Sorted List: ")
print(lst)
∂2