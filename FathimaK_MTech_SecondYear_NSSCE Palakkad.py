import turtle
import math

def draw_circle(t, radius, color):
    t.penup()
    t.goto(0, -radius)  # Move turtle to the bottom of the circle's center
    t.setheading(0)  # Ensure the turtle faces the default direction
    t.pendown()
    t.color(color)  # Set both pen and fill color to the same
    t.begin_fill()
    t.circle(radius)  # Draw circle with the center at (0, 0)
    t.end_fill()
    t.penup()  # Lift pen to avoid drawing when moving the turtle

# Function to draw a rectangle from the center (0, 0)
def draw_rectangle(t, width, height, color):
    t.penup()
    t.goto(0, 0)  # Move the turtle to the starting point (0, 0)
    t.pendown()
    t.fillcolor(color)  # Set the fill color
    t.pencolor(color)  # Set the pen color to match the fill color (removes border)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)  # Draw forward by the width
        t.left(90)
        t.forward(height)  # Draw upward by the height
        t.left(90)
    t.end_fill()
    t.penup()  # Lift pen to avoid drawing when moving the turtle

# Function to draw repeated and rotated rectangles
def draw_rotated_rectangles(t, width, height, color, repeat_count, rotate_angle, initial_rotation=0):
    t.setheading(initial_rotation)  # Set the initial rotation angle
    for _ in range(repeat_count):
        draw_rectangle(t, width, height, color)  # Draw the rectangle starting at (0, 0)
        t.right(rotate_angle)  # Rotate turtle by the specified angle

def draw_square(t, side, color):
    t.fillcolor(color)  # Set the fill color
    t.pencolor(color)  # Set the pen color to match the fill color (removes border)
    t.begin_fill()
    for _ in range(4):  # Draw a square
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.penup()

def draw_rotated_squares(t, side, color, repeat_count, rotate_angle, initial_rotation=0):
    t.setheading(initial_rotation)  # Set the initial rotation angle
    for _ in range(repeat_count):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        draw_square(t, side, color)  # Draw the square
        t.right(rotate_angle + 90)  # Rotate turtle for the next square

def square_spiral(x, y, pen, color):
    pen.goto(x, y)
    pen.down()
    pen.color("black")  # Set the turtle color
    pen.fillcolor(color)  # Set the fill color
    pen.begin_fill()

    # Outer loop to repeat the shape
    for _ in range(15):
        # Inner loop to draw a square
        for _ in range(4):
            pen.forward(15)  # Move forward by 100 units
            pen.right(90)     # Turn right by 90 degrees
        pen.right(24)
    pen.end_fill()
    pen.penup()

def main(t):
    # Your program logic goes here
    t.speed(0)  # Set turtle speed to max
    draw_circle(t, 310, "black")
    draw_circle(t, 300, "yellow")

    # Outer layer
    draw_rotated_rectangles(t, 210, 210, "brown", 36, 50)
    draw_rotated_rectangles(t, 195, 195, "red", 36, 50, 15)
    draw_rotated_rectangles(t, 180, 180, "orange", 36, 50)
    draw_rotated_rectangles(t, 165, 165, "yellow", 36, 50, 15)
    draw_rotated_rectangles(t, 150, 150, "white", 36, 50)

    draw_circle(t, 190, "orange")
    draw_circle(t, 170, "#ba1b09")
    draw_circle(t, 150, "#7d1004")
    square_spiral(0, 170, t, "white")
    square_spiral(0, -170, t, "white")
    square_spiral(145, 85, t, "white")
    square_spiral(-145, -85, t, "white")
    square_spiral(-145, 85, t, "white")
    square_spiral(145, -85, t, "white")

    # Middle Layer
    draw_rotated_rectangles(t, 135, 135, "green", 6, 60, 15)  # White rectangle with gold stroke equivalent
    draw_rotated_rectangles(t, 125, 125, "#ba1b09", 6, 60, 15)  # #ba1b09 color (dark red)
    draw_rotated_rectangles(t, 115, 115, "red", 6, 60, 15)  # Red rectangle layer

    # Drawing the square layers
    draw_rotated_squares(my_pen, 107, "#f4ff59", 12, 60, 15)  # s0
    draw_rotated_squares(my_pen, 97, "orange", 12, 60)  # s1
    draw_rotated_squares(my_pen, 79, "#ba1b09", 12, 60, 15)  # s2
    draw_rotated_squares(my_pen, 65, "#7d1004", 12, 60)  # s3

    draw_circle(t, 40, "yellow")  # c2: yellow circle
    draw_circle(t, 35, "green")  # c3: green circle
    draw_circle(t, 30, "white")  # c4: white circle

    # Inner layer: 
    square_spiral(0, 0, t, "pink")
    # Finish up
    my_window.mainloop()

# This ensures that main() is called only when this script is run directly
if __name__ == "__main__":  
    my_window = turtle.Screen()
    my_window.bgcolor("white")

    my_pen = turtle.Turtle()
    my_pen.speed(0)  # Set turtle speed to max
    main(my_pen)
    turtle.done()
