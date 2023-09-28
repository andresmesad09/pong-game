from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10

    def move(self, direction):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.increase_speed()

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
