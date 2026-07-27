# M2L6ACP: Drawing a Square in Turtle
# After Class Project: Custom Filled Square in Turtle Graphics

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L6ACP - Filled Square")
screen.bgcolor("lightgray")

t.color("purple", "orange")
t.pensize(4)

t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

print("Square ACP drawing completed!")
turtle.done()
