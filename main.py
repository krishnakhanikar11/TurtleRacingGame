from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race?Make a bet: ")
colors = ["red","yellow", "orange" ,"green", "blue", "purple"]

x_axis = -230
y_axis = -100

all_turtle=[]
for color in colors:
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(color)
    newTurtle.penup()
    newTurtle.goto(x_axis, y_axis)
    y_axis = y_axis + 30
    all_turtle.append(newTurtle)

is_game_on = False

if user_bet:
    is_game_on = True

while is_game_on:
    if newTurtle.xcor()>230:
       is_game_on = False
       race_winner = turtle.pencolor()
       if race_winner == user_bet:
           print(f"You've won the bet! The winner is {race_winner} color.")
       else:
           print(f"You have lost! The winner is {race_winner}")


    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
