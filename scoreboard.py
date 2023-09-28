from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_scores(self):
        self.l_score += 1
        self.update_scoreboard()
        self.clear()
        self.goto(0, 0)
        self.write("Left player scores", align=ALIGNMENT, font=FONT)
        time.sleep(0.5)
        self.update_scoreboard()

    def r_scores(self):
        self.r_score += 1
        self.update_scoreboard()
        self.clear()
        self.goto(0, 0)
        self.write("Right player scores", align=ALIGNMENT, font=FONT)
        time.sleep(0.5)
        self.update_scoreboard()