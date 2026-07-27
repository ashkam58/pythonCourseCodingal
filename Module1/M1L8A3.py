# M1L8A3: Color Spiral Pattern
# Activity 3: Drawing a multi-color spiral using turtle graphics

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M1L8A3 - Color Spiral Pattern")
screen.bgcolor("black")
t.speed(0)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for x in range(100):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x * 2)
    t.left(59)

print("Spiral pattern completed.")
turtle.done()
