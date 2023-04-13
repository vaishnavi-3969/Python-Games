import turtle

# defining constants
width = 500
height = 500
delay = 20  # milliseconds


def move_turtle():
    stamper.forward(1)
    stamper.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)

# creating window for drawing
screen = turtle.Screen()
screen.setup(width, height)
screen.title("My first turtle program")
screen.bgcolor("yellow")
screen.tracer(0)  # turns off automatic animation

# creating turtle to do bidding
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("red")
stamper.shapesize(50/20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10/20)
stamper.goto(100,100)
stamper.stamp()

move_turtle()

# end of program
turtle.done()

'''
use of turtle graphic stamps
1. board games
2. 2-D games: snakes/ trons clones
3. exploring mazes
4. pixel arts
'''