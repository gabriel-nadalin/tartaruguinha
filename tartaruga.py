import turtle as t
from random import random

x_bound, y_bound = t.screensize()
angle = int(25)
t.right(angle)
t.speed(speed=10)
while True:
    t.forward(1)
    if t.xcor() >= x_bound:
        pass
t.mainloop()