import turtle
import math

# Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("3D Rotating Cube")

screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("cyan")
t.pensize(2)

# Cube vertices
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Cube edges
edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

scale = 120

angle = 0

while True:

    t.clear()

    projected = []

    for v in vertices:

        x, y, z = v

        # Rotate around Y-axis
        x1 = x * math.cos(angle) - z * math.sin(angle)
        z1 = x * math.sin(angle) + z * math.cos(angle)

        # Rotate around X-axis
        y1 = y * math.cos(angle) - z1 * math.sin(angle)
        z2 = y * math.sin(angle) + z1 * math.cos(angle)

        # Perspective projection
        distance = 4
        factor = distance / (distance - z2)

        X = x1 * factor * scale
        Y = y1 * factor * scale

        projected.append((X, Y))

    # Draw edges
    for edge in edges:

        start = projected[edge[0]]
        end = projected[edge[1]]

        t.penup()
        t.goto(start)
        t.pendown()
        t.goto(end)

    screen.update()

    angle += 0.03