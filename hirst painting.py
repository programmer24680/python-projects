import random
import turtle
import colorgram
i = -750
j = -400
pen = turtle.Turtle()
pen.speed("fastest")
screen = turtle.Screen()
screen.colormode(255)
pen.penup()
pen.setposition(i, j)
colors = colorgram.extract("hirst.jpg", 6)
lst = [[color.rgb[i] for i in range(3)]for color in colors]
while True:
    random_color = random.choice(lst)
    pen.pendown()
    pen.dot(50, tuple(random_color))
    pen.penup()
    if i in range(-750, 750) and j in range(-400, 400):
        pen.forward(60)
        i += 60
    else:
        if i in range(725, 750) and j in range(370, 400):
            break
        else:
            i = -750
            j += 60
            pen.setposition(i, j)


screen.exitonclick()
