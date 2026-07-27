# M2L6A3: Turtle Color Spiral
# Activity 3: Drawing a multi-color geometric spiral

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L6A3 - Color Spiral Pattern")
screen.bgcolor("black")
t.speed(0)

colors = ["red", "magenta", "blue", "cyan", "green", "yellow"]

for i in range(80):
    t.pencolor(colors[i % 6])
    t.forward(i * 3)
    t.left(59)

print("Spiral pattern completed!")
turtle.done()
