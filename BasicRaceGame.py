import turtle
import random

turtle.title("Race Game")

player1 = turtle.Turtle()
player1.color("red")
player1.shape("turtle")
player1.penup()
player1.goto(-200,100)

player2 = player1.clone()
player2.color("blue")
player2.penup()
player2.goto(-200,-100)

player1.goto(300, 60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200,100)

player2.goto(300,-140)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200, -100)

die = [1,2,3,4,5,6]

for i in range(20):
    if player1.pos() >= (300,100):
        print("Player 1 Wins!")
        break
    elif player2.pos() >= (300,-100):
        print("Player 2 Wins!")
        break
    else:
        player1_turn = input("\nPlayer 1: Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player1.fd(20 * die_outcome)

        player2_turn = input("\nPlayer 2: Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player2.fd(20 * die_outcome)


turtle.hideturtle()
turtle.done()
