import turtle

# defining constants
width = 500
height = 500
delay = 20  # milliseconds


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)


# creating window for drawing
screen = turtle.Screen()
screen.setup(width, height)
screen.title("My first turtle program")
screen.bgcolor("yellow")
screen.tracer(0)  # turns off automatic animation

# creating turtle to do bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# # turtle awaits for our command
# my_turtle.forward(1000)

# set animattion in motion
move_turtle()

# end of program
turtle.done()
