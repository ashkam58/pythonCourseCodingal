# M1L8A2: Polygon Drawing with Loops
# Activity 2: Drawing any polygon (e.g., Pentagon/Hexagon) using turtle and loops

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M1L8A2 - Drawing a Polygon")
screen.bgcolor("lightyellow")

sides = 6
side_length = 80
angle = 360 / sides

t.color("purple")
t.pensize(3)

for _ in range(sides):
    t.forward(side_length)
    t.left(angle)

print("Polygon drawing completed.")
turtle.done()
