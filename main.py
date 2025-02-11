import turtle
import math

def draw_cloud(x, y, size=40):
    """Draw a cloud at the specified x, y coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    # turtle.pendown()
    
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.circle(size)
        turtle.forward(size)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color="black"):
    """
    Draw a filled rectangle starting from (x, y).
    (x, y) will be the bottom-left corner of the rectangle.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(x, y, base, color):
    """
    Draw an equilateral triangle with the given base length.
    The triangle’s base starts at (x, y) and extends to the right.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(base)
        turtle.left(120)
    turtle.end_fill()

def draw_tree(x, y, trunk_width=20, trunk_height=40, foliage_base=60):
    """
    Draw a tree using the draw_rectangle and draw_triangle functions.
    The (x, y) coordinate represents the center of the trunk’s bottom.
    """
    trunk_color = "saddlebrown"
    foliage_color = "forestgreen"
    
    # Draw the trunk.
    # Since draw_rectangle starts drawing from the bottom-left,
    # adjust x to center the trunk.
    draw_rectangle(x - trunk_width/2, y, trunk_width, trunk_height, trunk_color)
    
    # Draw the foliage (triangle) on top of the trunk.
    # Center the triangle by subtracting half of the foliage base.
    draw_triangle(x - foliage_base/2, y + trunk_height, foliage_base, foliage_color)

def draw_house():
    """Draw a house with a sky, evenly spaced windows, door, garage, roof, clouds, and 2 trees."""
    # --- Screen and House Setup ---
    screen_width = 800
    screen_height = 1200  # Increase the height so that the roof fits nicely
    house_width = 400
    house_height = 200
    door_width = 50
    door_height = 100
    garage_width = 75
    garage_height = 75
    window_size = 25

    # Define how much of the screen’s vertical space is ground.
    ground_height = screen_height / 3  # lower third will be green ground

    # Place the house so that its base sits at the top of the ground.
    # The screen’s bottom is at -screen_height/2.
    house_y = -screen_height/2 + ground_height
    house_x = -house_width / 2  # center the house horizontally

    # --- Draw Background and Ground ---
    # Set the sky as the background color (this ensures it covers the entire screen)
    turtle.bgcolor("lightblue")
    
    # Draw the ground (a rectangle starting from the bottom of the screen)
    draw_rectangle(-screen_width / 2, -screen_height / 2, screen_width, ground_height, "green")
    
    # --- Draw Trees ---
    # Draw two trees: one to the left of the house and one to the right.
    # For the left tree, position it 100 pixels left of the house;
    # for the right tree, 100 pixels to the right.
    draw_tree(house_x - 100, house_y, trunk_width=20, trunk_height=40, foliage_base=60)
    draw_tree(house_x + house_width + 100, house_y, trunk_width=20, trunk_height=40, foliage_base=60)
    
    # --- Draw the House and Roof ---
    # Draw the house’s main rectangular frame
    draw_rectangle(house_x, house_y, house_width, house_height, "beige")
    
    # Draw the roof (an equilateral triangle with the base along the top of the house)
    draw_triangle(house_x, house_y + house_height, house_width, "red")
    
    # --- Draw Evenly Spaced Windows (2×2 grid) ---
    # Compute positions for a left and a right column...
    left_window_x = house_x + house_width/4 - window_size/2
    right_window_x = house_x + (3*house_width)/4 - window_size/2
    # ...and for a top and a bottom row.
    top_window_y = house_y + (3*house_height)/4 - window_size/2
    bottom_window_y = house_y + house_height/4 - window_size/2

    # Draw the four windows.
    draw_rectangle(left_window_x, top_window_y, window_size, window_size, "white")   # Top left
    draw_rectangle(right_window_x, top_window_y, window_size, window_size, "white")  # Top right
    draw_rectangle(left_window_x, bottom_window_y, window_size, window_size, "white")# Bottom left
    draw_rectangle(right_window_x, bottom_window_y, window_size, window_size, "white")# Bottom right
    
    # --- Draw the Door and Garage Doors ---
    # Draw the door (centered along the front of the house)
    door_x = -door_width/2
    door_y = house_y
    draw_rectangle(door_x, door_y, door_width, door_height, "brown")
    
    # Draw the garage doors on the left and right sides of the house.
    draw_rectangle(house_x, house_y, garage_width, garage_height, "white")
    draw_rectangle(house_x + house_width - garage_width, house_y, garage_width, garage_height, "white")
    
    # --- Draw Clouds in the Sky ---
    # Place clouds relative to the overall screen size.
    draw_cloud(-screen_width/3, 220)  # one cloud in the left portion of the sky
    draw_cloud(screen_width/4, 120)   # another cloud on the right

def main():
    turtle.speed(0)  # Fast drawing
    draw_house()
    turtle.done()

main()