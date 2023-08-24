import turtle
from random import *

t = turtle.Turtle()
llx = -100
lly = -100
urx = 100
ury = 100
turtle.setworldcoordinates(llx, lly, urx, ury)

x_bound, y_bound = turtle.screensize()
angle = randint(0, 360)
t.seth(angle)
t.speed(10)
while True:
    t.forward(5)
    if t.xcor() >= urx or t.xcor() <= llx: t.seth(180 - t.heading())
    if t.ycor() >= ury or t.ycor() <= lly: t.seth(360 - t.heading())