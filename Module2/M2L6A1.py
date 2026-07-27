# M2L6A1: Intro to Turtle - Drawing a Square
# Activity 1: Turtle Graphics Canvas Setup & Square Drawing

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L6A1 - Turtle Canvas & Square")
screen.bgcolor("lightblue")

t.color("navy")
t.pensize(3)

# Draw Square
for _ in range(4):
    t.forward(120)
    t.right(90)

print("Square drawing completed successfully!")
turtle.done()
