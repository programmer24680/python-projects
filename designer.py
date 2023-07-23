import turtle
import random

directions = [0, 90, 180, 270]
turtle.speed(25000)
turtle.pensize(10)
while True:
    turtle.color((random.random(), random.random(), random.random()))
    turtle.pendown()
    turtle.forward(25)
    turtle.right(random.choice(directions))
