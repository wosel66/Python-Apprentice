""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""
import turtle


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "leagebot_bolt.gif")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

t.pencolor('blue')
t.pendown()
t.speed(3)

for i in range(6):
   t.forward(75)
   t.left(45)

turtle.exitonclick()


... # Your Code Here