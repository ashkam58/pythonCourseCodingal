# M2L7A2: Turtle Star & Snowflake Patterns
# Activity 2: Drawing Stars using Functions and Angle Calculations

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L7A2 - Star Snowflake")
screen.bgcolor("darkblue")
t.color("cyan")
t.speed(0)

def draw_star(size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

for i in range(8):
    draw_star(80)
    t.right(45)

print("Star snowflake completed!")
turtle.done()
