#Prompt the user to enter the time

Time = (eval(input("Enter an integer for seconds: ")))
Minutes = Time // 60
Seconds = Time%60

print(Time, "Second is ",Minutes, "minutes and ",Seconds)
