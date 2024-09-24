"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
tina.pendown()
tina.begin_fill
tina.color("blue")
tina.forward(204)
tina.color("green")
tina.left(135)
tina.penup()

tina.pendown()
tina.forward(150)
tina.color("red")
tina.end_fill
tina.left(90)
tina.penup()

tina.pendown()
tina.forward(150)


# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
