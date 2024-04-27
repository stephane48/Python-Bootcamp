import random
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()


#Graphic to draw dashed line
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#Random color
color_figure = ["red", "blue", "purple", "pink", "green", "orange", "yellow", "brown"]



#Draw a triangle
def triangle():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for _ in range(3):
        timmy_the_turtle.right(120)
        timmy_the_turtle.forward(100)

#Draw a square
def square():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(4):
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)

#Draw pentagon
def pentagon():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(5):
        timmy_the_turtle.right(72)
        timmy_the_turtle.forward(100)

#Draw hexagon
def hexagon():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(6):
        timmy_the_turtle.right(60)
        timmy_the_turtle.forward(100)

#draw heptagon
def heptagon():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(7):
        timmy_the_turtle.right(51.42)
        timmy_the_turtle.forward(100)

#Draw octagon
def octagon():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(8):
        timmy_the_turtle.right(45)
        timmy_the_turtle.forward(100)

#Draw nonagon
def nonagon():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(9):
        timmy_the_turtle.right(40)
        timmy_the_turtle.forward(100)

#Draw decagon
def decagon():
    timmy_the_turtle.color(random.choice(color_figure)) # pick color from list
    for i in range(10):
        timmy_the_turtle.right(36)
        timmy_the_turtle.forward(100)

#Draw all the figures
triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()
