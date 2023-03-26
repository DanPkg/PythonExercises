# Draw a flower like shape with pentagons
import turtle

turtle.speed(12)

PENTAGON_SIDES = 5
PENTAGON_ANGLE_EXT = 72

def draw_pentagon(pent_color, side_length):
    
    turtle.pencolor(pent_color)
    for i in range(8):
        
        for j in range(PENTAGON_SIDES):
            turtle.forward(side_length)
            turtle.left(PENTAGON_ANGLE_EXT)
        
        turtle.left(45)         

draw_pentagon('red', 120)
draw_pentagon('blue', 160)
turtle.done()



# Course coordinator's code:
import turtle

TILT_ANGLE = 45
num_of_polygons = int(360 / TILT_ANGLE)

turtle.showturtle()
turtle.speed(9)

turtle.pencolor('orange red')

sides = 5  # pentagons in lower layer
side_length = 110
for i in range(num_of_polygons):
    # Inner loop, draws a single polygon
    for j in range(sides):
        turtle.forward(side_length)
        turtle.left(360/sides)

    turtle.left(TILT_ANGLE)

turtle.pencolor('blue')

sides = 6  # hexagons in overlay
side_length = 120
for i in range(num_of_polygons):
    for j in range(sides):
        turtle.forward(side_length)
        turtle.left(360/sides)

    turtle.left(TILT_ANGLE)

turtle.hideturtle()
turtle.done()
