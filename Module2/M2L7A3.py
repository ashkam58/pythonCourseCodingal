# M2L7A3: Turtle Flower Mandala Pattern
# Activity 3: Drawing a Mandala / Flower using repeated circle rotations

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L7A3 - Turtle Flower Mandala")
screen.bgcolor("black")
t.speed(0)

colors = ["red", "yellow", "blue", "green", "pink", "orange"]

for i in range(36):
    t.pencolor(colors[i % 6])
    t.circle(80)
    t.left(10)

print("Flower mandala drawing completed!")
turtle.done()
