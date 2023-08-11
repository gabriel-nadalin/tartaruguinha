import turtle
from random import *
import keyboard

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
    if keyboard.read_key() == "d":
        t.setheading(0)
        t.forward(10)
t.mainloop()