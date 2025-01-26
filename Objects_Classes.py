import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        #calculate and print the area of the circle
        circle_area = math.pi * self.radius ** 2
        print(f"The area of the circle is: {circle_area:.2f}")

    def perimeter(self):
        #calculate and print the perimeter of the circle
        circle_perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle is: {circle_perimeter:.2f}")

#the user will input the radius
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

circle.area()
circle.perimeter()
