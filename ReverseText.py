# Reverse Text using Function
def reverseText():
    while(True):
        user = str(input("Enter a string: "))
        if user.replace(" ", "").isalpha():     # add spaces and method to check if the user's input contained alphabet
            reversed_text = user[::-1]                      # slicing method
            print("Output: ", reversed_text)
            break
        else:
            print("Error Reported! Enter text only.\n")

reverseText()


