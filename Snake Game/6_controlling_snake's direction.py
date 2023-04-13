import turtle

# defining constants
width = 500
height = 500
delay = 100  # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


# defining functions
def move_turtle():
    stamper.forward(1)
    stamper.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)


def move_snake():
    stamper.clearstamps()  # remove existing stamps
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

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

def go_up():
    global snake_direction
    if snake_direction!= "down":
        snake_direction = 'up'


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = 'down'


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = 'right'


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = 'left'


# creating window for drawing
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("yellow")
screen.tracer(0)  # turns off automatic animation

# event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.onkey(go_down, "Down")

# creating turtle to do bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("green")
stamper.penup()

# snake as a list of coordinate pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0], [80, 0]]
snake_direction = 'up'  # global variable

# draw snake for 1st time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# set animation in motion
move_snake()

# end of program
turtle.done()
