from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
# turn off traces
screen.tracer(0)
screen.title("Pong game")

r_paddle = Paddle(start_x=350, start_y=0)
l_paddle = Paddle(start_x=-350, start_y=0)
ball = Ball()
scoreboard = ScoreBoard()
scoreboard.update_scoreboard()
screen.update()

# Listen the arrow keys
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move(direction="up")
    print("Enter")
    print(ball.x_move)
    print(ball.y_move)

    # detect collision with borders
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("collision with borders")
        ball.bounce_y()

    # detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        print("collision with paddle")
        ball.bounce_x()

    # detect miss of right paddle
    if ball.xcor() > 380:
        print("r misses")
        ball.reset_position()
        scoreboard.l_scores()

    # detect miss of left paddle
    if ball.xcor() < -380:
        print("l misses")
        ball.reset_position()
        scoreboard.r_scores()

screen.exitonclick()
