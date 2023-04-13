import turtle

# defining constants
width = 500
height = 500
delay = 400  # milliseconds

def move_turtle():
    stamper.forward(1)
    stamper.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)


def move_snake():
    stamper.clearstamps()  # remove existing stamps
    new_head = snake[-1].copy()
    new_head[0] += 20

    #     add new head to snake body
    snake.append(new_head)

    #     remove last segment of snake
    snake.pop(0)
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    #     refresh screen
    screen.update()

    #     rinse and repeat
    turtle.ontimer(move_snake, delay)


# creating window for drawing
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("yellow")
screen.tracer(0)  # turns off automatic animation

# creating turtle to do bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("green")
stamper.penup()

# snake as a list of coordinate pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0], [80, 0]]

# draw snake for 1st time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# set animation in motion
move_snake()

# end of program
turtle.done()
