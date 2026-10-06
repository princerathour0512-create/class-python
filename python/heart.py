import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
t = turtle.Turtle()
t.speed(10)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

for i in range(120):
    t.penup()
    t.goto(0, 40)
    
    angle = i * (math.pi * 2) / 120
    
    # Heart shape parametric equations scaled by 15
    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15
    
    c = random.choice(colors)
    t.color(c)
    
    t.pendown()
    t.goto(x, y)
    
    # Draws small star-like bursts or textures at each point
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)
# screen.update()
# screen.mainloop()

turtle.done()
