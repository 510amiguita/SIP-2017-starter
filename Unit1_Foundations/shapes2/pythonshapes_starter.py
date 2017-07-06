from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -100

color = input("Enter a color: ")

if color == "red":
    t.pencolor("red")
elif color == "blue":
    t.pencolor("blue")
elif color == "green":
    t.pencolor("green")
elif color == "yellow":
    t.pencolor("yellow")

sides = 3;

for movement in range(sides):
    t.forward(100)
    t.left(360/sides)









# Close window on click.
exitonclick()
