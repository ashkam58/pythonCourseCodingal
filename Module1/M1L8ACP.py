# M1L8ACP: Turtle Star Pattern ACP
# After Class Project: Drawing a colorful 5-pointed star

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M1L8ACP - Turtle Star")
screen.bgcolor("darkblue")

t.color("yellow")
t.pensize(3)

t.begin_fill()
for _ in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

print("Star ACP completed.")
turtle.done()
