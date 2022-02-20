import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle = Turtle("square")
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_wid=5.0, stretch_len=1.0)
paddle.goto(350, 0)
screen.update()
# time.sleep(0.1)


screen.exitonclick()