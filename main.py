import turtle
from drawing import draw_cloud, draw_rectangle, draw_triangle, draw_tree, draw_house

def main():
    turtle.speed(0)  # Fast drawing
    draw_house()
    turtle.done()

if __name__ == "__main__":
    main()