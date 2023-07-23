import turtle
import random
colors = ["red", "blue", "yellow", "crimson", "black", "violet", "pink", "coral", "papaya whip", "indigo"]
directions = [0, 90, 180, 270]
turtle.speed(25000)
turtle.pensize(10)
while True:
    turtle.color(random.choice(colors))
    turtle.pendown()
    turtle.forward(25)
    turtle.right(random.choice(directions))
