# Define dictionaries for four students
students = [
    {
        "name": "Aaron Enright",
        "major": "Library and Information Science",
        "favorite_food": "pizza",
        "favorite_color": "blue"
    },
    {
        "name": "Alan Rubel",
        "major": "Philosophy",
        "favorite_food": "mac and cheese",
        "favorite_color": "red"
    },
    {
        "name": "Ken Ampilodt",
        "major": "Programming",
        "favorite_food": "chicken",
        "favorite_color": "black"
    },
    {
        "name": "Allen Ross",
        "major": "Math",
        "favorite_food": "lechon",
        "favorite_color": "pink"
    }
]

# List of ordinal strings for the first four numbers
orders = ["first", "second", "third", "fourth"]

# Function to print student information
def print_student_info(student, index):
    order = orders[index]  # Get the ordinal string
    print("The " + order + " student's name is " + student['name'] + ".")
    print("The " + order + " student's major is " + student['major'] + ".")
    print("The " + order + " student's favorite food is " + student['favorite_food'] + ".")
    print("The " + order + " student's favorite color is " + student['favorite_color'] + ".")
    print()  # Print a blank line between students

# Print information for all students
for i, student in enumerate(students):
    print_student_info(student, i)
