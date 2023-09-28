from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__(shape='square')
        # start at 20,20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=start_x, y=start_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
