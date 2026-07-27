# M2L7A1: Turtle Functions & Rainbow Circles
# Activity 1: Modular Turtle Drawing with Functions

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L7A1 - Concentric Circles")
screen.bgcolor("black")
t.speed(0)

def draw_circle(radius, color):
    t.pencolor(color)
    t.circle(radius)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
radius = 20

for color in colors:
    draw_circle(radius, color)
    radius += 15

print("Concentric circles drawing completed!")
turtle.done()
