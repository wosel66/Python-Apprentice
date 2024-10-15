import turtle
turtle.setup(width =600, height=600)

w = turtle.Turtle()

w.shape('turtle')
w.speed(2)

for i in range(4):
    w.forward(150)
    w.left(90)
    
turtle.exitonclick()