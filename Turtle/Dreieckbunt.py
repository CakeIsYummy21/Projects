import turtle
import random
turtle.colormode(255)
turtle.forward(1)
turtle.left(120)
turtle.width(3)
turtle.speed(-1)
turtle.hideturtle()
d = 0
for a in range(1,10000,3):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    turtle.color(r , g, b)
    d = (d + 0.001)
    turtle.forward(a)
    turtle.left(120 - d)
    turtle.color(round(r / 1.4), round(g / 1.4), round(b / 1.4))
    turtle.forward(a + 1)
    turtle.left(120 - d)
    turtle.color(round(r / 1.8), round(g / 1.8), round(b / 1.8))
    turtle.forward(a + 2)
    turtle.left(120 - d)
input()