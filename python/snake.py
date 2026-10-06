import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Screen
wn = turtle.Screen()
wn.title("Snake Game by Prince")
wn.bgcolor("black")
wn.setup(width=2000, height=1000)
wn.tracer(0)

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0",
          align="center",
          font=("Arial", 20, "bold"))

segments = []

# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(y - 20)

    if head.direction == "left":
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(x + 20)

# Keyboard
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main Game Loop
while True:

    wn.update()

    # Border Collision
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):

        time.sleep(1)

        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Arial", 20, "bold"))

    # Food Collision
    if head.distance(food) < 20:

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()

        segments.append(new_segment)

        delay -= 0.002

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Arial", 20, "bold"))

    # Move Body
    for i in range(len(segments)-1, 0, -1):

        x = segments[i-1].xcor()
        y = segments[i-1].ycor()

        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self Collision
    for segment in segments:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)
            head.direction = "stop"

            for s in segments:
                s.goto(1000, 1000)

            segments.clear()

            score = 0
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center",
                      font=("Arial", 20, "bold"))

    time.sleep(delay)