import time
import turtle
def up():
    turtle.setheading(90)
    turtle.forward(10)
def right():
    turtle.setheading(0)
    turtle.forward(10)
def down():
    turtle.setheading(270)
    turtle.forward(10)
def left():
    turtle.setheading(180)
    turtle.forward(10)
def clearall():
    turtle.clear()
def penup():
    turtle.penup
def pendown():
    turtle.pendown
turtle.onkeypress(up, 'w')
turtle.onkeypress(down, 's')
turtle.onkeypress(left, 'a')
turtle.onkeypress(right, 'd')
turtle.onkeypress(clearall, 'space')
turtle.onkeypress(penup, 'q')
turtle.onkeypress(pendown, 'e')
turtle.speed(-1)
turtle.listen()
input()