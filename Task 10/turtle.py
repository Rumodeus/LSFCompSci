# Alphabet program

# -------------------------
# Import libraries
# -------------------------
import turtle


# -------------------------
# Subprograms
# -------------------------
def draw_letter(letter):
    # Draw letter C
    if letter == "C":
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(180)
    if letter == "F":
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(80)
 

# -------------------------
# Main program
# -------------------------
turtle.pensize(5)
draw_letter("F")
turtle.done()
