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


# function to draw a rectangle with specified starting position
def draw_rectangle(start,width, height):

    # Lift the pen to avoid drawing
    turtle.penup()

    turtle.goto(start)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    



#draw 2 windows
draw_rectangle((-150, -100), 50, 50)
draw_rectangle((100, -100), 50, 50)

turtle.done()