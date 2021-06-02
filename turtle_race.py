from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle(num):
    x = -230
    y = -130
    turtles = []
    position = 0
    for _ in range(num):
        y += 40
        turtles.append(Turtle(shape="turtle"))
        turtles[_].penup()
        turtles[_].color(colors[position])
        turtles[_].goto(x, y)
        position += 1
    return turtles


all_turtles = create_turtle(6)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
