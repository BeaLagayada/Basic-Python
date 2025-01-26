s1 = set()
s2 = {1, 3, 5}
s3 = set([1,3,5])
s4 = set([x * 2 for x in range(1, 5)])
s6 = set("beagwapa")

#for i in range(0,10):
    #s5 = eval(input("enter a set: "))
    #s1.add(s5)

#print(s1)
print(s2)
print(s3)
print(s4)
print(s6)
print(len(s6))
s2.remove(3)
print(s2)

s7 = {1,2,4}
s8 = {1,4,2,3,6}
sub = s7.issubset(s8)
print(sub)
sub = s7.issuperset(s8)
print(sub)
inter = s8.intersection(s7)
print(inter)
inter = s7.intersection(s8)
print(inter)
diff = s8.difference(s7)
print(diff)
sym = s8.symmetric_difference(s7)
print(sym)

students = {"peter", "john"}
print(students)
students.add("john")
print(students)
students.add("peterson")
print(students)
students.remove("peter")
print(students)
students.remove("johnson")
print(students) #Yes it will have a keyerror: 'johnson'


