import turtle


#flower = turtle.Turtle()
#turtle.bgcolor("pink")
#flower.speed(0.5)
#flower.pensize(2)
#flower.shape("turtle")

#color = ["Violet", "Red", "Yellow", "Blue", "Green"]
#for i in range(150):
    #for c in color:
     #   flower.color(c)
      #  flower.circle(180, 100)
       # flower.left(90)
        # flower.right(100)
        # flower.end_fill()

#flower.hideturtle()
#turtle.done()

face = turtle.Turtle()
turtle.bgcolor("pink")
face.speed(3)
face.shape("turtle")

face.penup()
face.goto(0,-300)
face.pendown()
face.begin_fill()
face.fillcolor("yellow")
face.circle(300) #big circle
face.end_fill()

face.penup()
face.goto(-120,100)
face.pendown()
face.begin_fill()
face.color("green")
face.circle(50)
face.end_fill()
face.penup()
face.goto(120,100)
face.pendown()
face.begin_fill()
face.color("green")
face.circle(50)
face.end_fill() #small circle

face.penup()
face.goto(0, -50)
face.pendown()
face.begin_fill()
face.color("blue")
face.circle(50, steps=3)
face.end_fill() #triangle

face.penup()
face.goto(-90,-140)
face.pendown()
face.begin_fill()
face.color("red")
face.right(90)
face.circle(90,180)
face.end_fill() #smile

face.penup()
face.goto(-55,-140)
face.pendown()
face.begin_fill()
face.color("white")
face.right(-180)
face.circle(55,180)
face.end_fill()


face.hideturtle()
turtle.done()






