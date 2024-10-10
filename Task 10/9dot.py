# Nine dot program

# -------------------------
# Import libraries
# -------------------------
import turtle


# -------------------------
# Subprograms
# -------------------------
def draw_dots():
    for y in range(0, 150, 50):
        for x in range(0, 150, 50):
            turtle.setposition(x, y)
            turtle.pendown()
            turtle.dot(20)
            turtle.penup()
    turtle.home()
    turtle.pendown()


def move(x, y):
    turtle.setposition(x * 50, y * 50)


# -------------------------
# Main program
# -------------------------
draw_dots()
# Line 1
move(2, 2)
# Line 2
move(-1, 2)
# Line 3
move(2, -1)
# Line 4
move(2, 2)
turtle.done()
