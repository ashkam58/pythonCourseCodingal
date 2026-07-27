# M2L7ACP: Turtle Masterpiece Art ACP
# After Class Project: Custom Turtle Geometric Masterpiece

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("M2L7ACP - Geometric Masterpiece")
screen.bgcolor("black")
t.speed(0)

colors = ["gold", "deepskyblue", "coral", "limegreen", "violet"]

for i in range(120):
    t.pencolor(colors[i % 5])
    t.forward(i * 1.5)
    t.right(98)

print("Geometric masterpiece completed!")
turtle.done()
