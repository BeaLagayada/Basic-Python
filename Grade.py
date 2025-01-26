#Prompt User to Input Personal Information
StudentName = str(input("Student Name: "))
IDNum = int(input("ID Number: "))
Course = str(input("Course: "))
Section = str(input("Section: "))

#Prompt User to Input Quarter Grades
FirstQuarter = eval(input("Enter First Quarter Grade: "))
SecondQuarter = eval(input("Enter Second Quarter Grade: "))
ThirdQuarter = eval(input("Enter Third Quarter Grade: "))
FourthQuarter = eval(input("Enter Fourth Quarter Grade: "))

#Get the Average
Average = (FirstQuarter + SecondQuarter + ThirdQuarter + FourthQuarter) /4

print("StudentName: ", StudentName)
print("IDNumber: ", IDNum)
print("Course: ", Course)
print("Section: ", Section)

print("The Average of four quarter grades is ", Average)
