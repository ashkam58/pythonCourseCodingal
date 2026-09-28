# M2L6A2: Polygon Drawing in Turtle
# Activity 2: Drawing any polygon (Pentagon/Hexagon) using Turtle and Loops

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L6A2 - Turtle Hexagon")
screen.bgcolor("white")

sides = 6
side_length = 70
angle = 360 / sides

t.color("darkgreen")
t.pensize(2)

for _ in range(sides):
    t.forward(side_length)
    t.left(angle)

print("Hexagon drawing completed!")
turtle.done()
