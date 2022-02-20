from turtle import Turtle, Screen

screen = Screen()


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        screen.tracer(1)
        self.shape("circle")
        self.penup()
        # self.speed("slowest")
        self.color("white")
        # # self.setheading(45)
        # self.goto(330, 250)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
