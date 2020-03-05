import turtle

screen = turtle.Screen()

leonardo = turtle.Turtle()

for counter in range (180):
    if not counter % 2 == 0:
        leonardo.forward(50)
    else:
        leonardo.backward(10)
    leonardo.left(61)

screen.exitonclick()

