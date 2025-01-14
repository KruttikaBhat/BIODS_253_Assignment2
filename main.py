import turtle

# Draw main rectangle for house frame
turtle.penup()
turtle.goto(-200, -200)  # Starting position for house frame
turtle.pendown()

# Draw rectangle
for _ in range(2):
    turtle.forward(400)  # Width of house
    turtle.left(90)
    turtle.forward(200)  # Height of house
    turtle.left(90)

turtle.done()