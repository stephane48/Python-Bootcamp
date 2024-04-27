import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.speed("fastest")

#Spirograph Code
for i in range(72):
    tim.circle(100)
    tim.right(5)
    tim.pencolor(random_color())

# #Random Walk
# for _ in range(10000):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


screen = Screen()
screen.setup(800,800)
screen.exitonclick()
