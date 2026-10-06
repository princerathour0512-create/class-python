import turtle

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Makes the pink and brown stand out

t = turtle.Turtle()
t.speed(0)               # Fastest animation speed
t.left(90)               # Point the turtle upwards to grow the tree

def tree(i):
    if i < 15:
        return
    else:
        t.color("brown")
        t.forward(i)
        
        # Draw a small pink flower petal/circle at the branch fork
        t.color("red")
        t.circle(5)
        t.color("palegreen")  # Reset color to black for branches
        
        # Left branch
        t.left(20)
        tree(4 * i / 5)   # Recursive call with a shorter branch length
        
        # Right branch
        t.right(40)
        tree(4 * i / 5)   # Recursive call with a shorter branch length
        
        # Return to original orientation and position
        t.left(20)
        t.backward(i)

# Move turtle down slightly so the tree fits well on the screen
t.penup()
t.goto(0, -150)
t.pendown()

# Draw the tree starting with a trunk length of 100
tree(100)

# Keep the window open when finished
turtle.done()