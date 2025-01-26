import turtle

#turtle.Turtle()
#turtle.shape("turtle")
#turtle.speed(1)

#this creates a rectangle shape
#turtle.forward(300)
#turtle.right(90)
#turtle.forward(150)
#turtle.right(90)
#turtle.forward(300)
#turtle.right(90)
#turtle.forward(150)
#turtle.penup()

#creating multiple turtle
#turtle.bgcolor("sky blue")
#sanji = turtle.Turtle()
#sanji.penup()
#sanji.color("red")
#sanji.shape("turtle")
#sanji.goto(100,100)

#zoro = turtle.Turtle()
#zoro.color("green")
#zoro.shape("turtle")


pen = turtle.Turtle()
pen.pensize(3)
pen.penup() #pull the pen up
pen.speed(1)
pen.goto(-200,-50)
pen.pendown() #pull the pen down
pen.begin_fill()
pen.color("violet")
pen.circle(40, steps=3) #draw a triangle
pen.end_fill()

pen.penup()
pen.goto(-100, -50)
pen.pendown()
pen.begin_fill()
pen.color("green")
pen.circle(40, steps=4) #draw a square
pen.end_fill()

pen.penup()
pen.goto(0, -50)
pen.pendown()
pen.begin_fill()
pen.color("pink")
pen.circle(40, steps=5) #draw a pentagon
pen.end_fill()

pen.penup()
pen.goto(100, -50)
pen.pendown()
pen.begin_fill()
pen.color("yellow")
pen.circle(40, steps=6) #draw a hexagon
pen.end_fill()

pen.penup()
pen.goto(200, -50)
pen.pendown()
pen.begin_fill()
pen.color("red")
pen.circle(40) #draw a circle
pen.end_fill()

pen.penup()
pen.goto(-50, 50)
pen.pendown()
pen.color("black")
pen.write("Color Shapes", font=("times new roman", 20, "bold"))

pen.hideturtle()
turtle.done()

