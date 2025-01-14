import turtle

def draw_cloud(x, y):
    """Draw a cloud at the specified x, y coordinates"""
    turtle.penup()
    turtle.goto(x, y)
    
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.circle(30)
        turtle.forward(30)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color="black"):
    """Draw a filled rectangle starting from x, y coordinates"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Set up screen dimensions
screen_width = 800
screen_height = 600

# ----- GROUND AND SKY -----
# Draw sky
draw_rectangle(-screen_width/2, screen_height/2, screen_width, screen_height*2/3, "lightblue")
# Draw ground
draw_rectangle(-screen_width/2, -screen_height/6, screen_width, screen_height/3, "green")

# ----- HOUSE FRAME -----
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

# ----- CLOUDS -----
draw_cloud(-150, 100)
draw_cloud(50, 150)

turtle.done()