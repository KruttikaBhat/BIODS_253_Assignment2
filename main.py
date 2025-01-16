import turtle

def draw_triangle(tip, side_length, color):
    """
    Draws an equilateral triangle using the turtle module.

    Parameters:
    side_length (int or float): The length of each side of the triangle.
    """
    tip.fillcolor(color)
    tip.begin_fill() 
    for _ in range(3):
        tip.forward(side_length)  # Move forward by the specified side length
        tip.left(120)  # Turn the turtle 120 degrees to the left

    tip.end_fill()


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

turtle.penup()

turtle.goto(-400, -100)
draw_triangle(turtle, 100, "green")

turtle.done()