import turtle
import random
turtle.speed(-1)
turtle.hideturtle()
turtle.colormode(255)
def dot(x,y):
    turtle.goto(x,y)
    turtle.width(random.randint(0,255))
    turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.dot(random.randint(0,255))
while True:
    dot(random.randint(-1255,1255),random.randint(-1255,1255))