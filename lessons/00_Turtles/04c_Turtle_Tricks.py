"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.

"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

tina.pendown()
tina.color('orange')
tina.begin_fill()
tina.circle(95, steps=150 )
tina.end_fill()
tina.penup()

tina.
tina.pendown()
tina.color('blue')
tina.begin_fill()
tina.circle(20, steps=75)
tina.end_fill()
tina.circle(20)
# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes


... # Your code here

turtle.exitonclick()                    # Close the window when we click on it


# Dont forget to check in your code!