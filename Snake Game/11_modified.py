import math
import turtle
import random

# defining constants and variables
width = 500
height = 500
delay = 100  # milliseconds
food_size = 10
speed = 1
speed_increase_factor = 0.1
high_score = 0

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 1),
    "right": (20, 0)
}

colors = {
    "red": "#ff7f7f",
    "orange": "#ffb347",
    "yellow": "#ffff99",
    "green": "#90ee90",
    "blue": "#87cefa",
    "purple": "#d3d3e3"
}


# defining functions
def move_turtle():
    stamper.forward(1)
    stamper.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)


def food_collision():
    global food_pos, score, speed
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        speed += speed_increase_factor
        food_pos = get_random_food_pos()
        food.color(random.choice(list(colors.values())))
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(-width / 2 + food_size, width / 2 + food_size)
    y = random.randint(-height / 2 + food_size, height / 2 + food_size)
    return x, y


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = math.sqrt((math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2)))
    return distance


def game_loop():
    stamper.clearstamps()  # remove existing stamps
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # check collisions
    if new_head in snake or new_head[0] < -width / 2 or new_head[1] > width / 2 or new_head[1] < -height / 2 or \
            new_head[1] > height / 2:
        # turtle.bye()
        reset()
    else:
        #     add new head to snake body
        snake.append(new_head)

        # check food collision
        if not food_collision():
            snake.pop(0)  # keep snake the same length

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

            #     refresh screen
        screen.title(f"Snake Game, Score: {score}")
        screen.update()

        #     rinse and repeat
        turtle.ontimer(game_loop, delay)


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction('up'), "Up")
    screen.onkey(lambda: set_snake_direction('down'), "Down")
    screen.onkey(lambda: set_snake_direction('right'), "Right")
    screen.onkey(lambda: set_snake_direction('left'), "Left")


def set_snake_direction(direction):
    global snake_direction
    if direction == 'up':
        if snake_direction != 'down':
            snake_direction = "up"
    elif direction == 'down':
        if snake_direction != 'up':
            snake_direction = "down"
    elif direction == 'right':
        if snake_direction != 'left':
            snake_direction = "right"
    elif direction == 'left':
        if snake_direction != 'right':
            snake_direction = "left"


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0], [80, 0]]
    snake_direction = 'up'  # global variable
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()


# creating window for drawing
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("yellow")
screen.tracer(0)  # turns off automatic animation

# event handlers
screen.listen()
bind_direction_keys()

# creating turtle to do bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("green")
stamper.penup()

# food
food = turtle.Turtle()
food.shape('triangle')
food.shapesize(food_size / 20)
food.penup()

reset()

# end of program
turtle.done()
