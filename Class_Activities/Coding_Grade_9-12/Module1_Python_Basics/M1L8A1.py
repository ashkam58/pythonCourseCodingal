# M1L8A1: Turtle Canvas & Basic Shapes
# Activity 1: Setting up Turtle graphics screen and drawing a square

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M1L8A1 - Drawing a Square")
screen.bgcolor("black")
t.color("cyan")

# Draw square
for _ in range(4):
    t.forward(100)
    t.left(90)

print("Square drawing completed successfully.")
turtle.done()
