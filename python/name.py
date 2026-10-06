import turtle
import random
import time

# Screen Setup
screen = turtle.Screen()
screen.setup(600, 300)
screen.bgcolor("black")
screen.title("Animated Name")

screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

colors = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta", "white"]

# -------------------------
# Background Stars
# -------------------------
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.speed(0)

for _ in range(200):
    stars.goto(random.randint(-500, 500), random.randint(-300, 300))
    stars.dot(random.randint(2, 5), random.choice(colors))

screen.update()

# -------------------------
# Animated Name
# -------------------------
name = "PRINCE"
start_x = -190

for letter in name:
    pen.goto(start_x, 0)

    # Glow Effect
    for size in [0]:
    # for size in [70, 66, 62, 58, 54]:
        pen.color(random.choice(colors))
        pen.write(letter, align="center", font=("Courier", size, "bold"))
        screen.update()
        time.sleep(0.05)
        # pen.clear()

    # Final Letter
    pen.color("white")
    pen.write(letter, align="center", font=("Courier", 54, "bold"))

    start_x += 70
    screen.update()
    time.sleep(0.15)

# -------------------------
# Fireworks
# -------------------------
# fire = turtle.Turtle()
# fire.hideturtle()
# fire.speed(0)

# for _ in range(20):
#     x = random.randint(-300, 300)
#     y = random.randint(50, 220)

#     fire.penup()
#     fire.goto(x, y)

#     c = random.choice(colors)

#     for angle in range(0, 360, 20):
#         fire.setheading(angle)
#         fire.pendown()
#         fire.color(c)
#         fire.forward(20)
#         fire.backward(20)
#         fire.penup()

screen.update()

turtle.done()