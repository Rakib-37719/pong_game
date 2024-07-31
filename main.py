from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

SCREENWIDTH = 800
SCREENHEIGHT = 600

screen = Screen()
screen.bgcolor('black')
screen.addshape("football.gif")
screen.bgpic("bg_1.gif")
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.tracer(0)

l_paddle = Paddle((-360,0))
r_paddle = Paddle((360,0))


screen.listen()

screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')

ball = Ball()
ball.shape("football.gif")

game_is_on = True
x_dir = 1
y_dir = 1
l_score = 0
r_score = 0
while game_is_on:
    time.sleep(0.1)
    ball.move(x_dir,y_dir)

    if ball.ycor() == 250 or ball.ycor() == - 310:
        y_dir = - y_dir
    # elif ball.xcor() > 320 and ball.distance(r_paddle) < 60:
    #     x_dir = -x_dir
    # elif ball.xcor() < -320 and ball.distance(l_paddle) < 60:
    #     x_dir = -x_dir
    elif abs(l_paddle.xcor() - ball.xcor()) <50 and abs(l_paddle.ycor() - ball.ycor()) < 50:
        #print(abs(l_paddle.xcor() - ball.xcor()),abs(l_paddle.ycor() - ball.ycor()))
        x_dir = -x_dir
        l_score += 1
    elif abs(r_paddle.xcor() - ball.xcor()) <50 and abs(r_paddle.ycor() - ball.ycor()) < 50:
        x_dir = -x_dir
        r_score += 1
        #print(abs(r_paddle.xcor() - ball.xcor()),abs(r_paddle.ycor() - ball.ycor()))
    print(l_score, r_score)
    screen.update()


screen.exitonclick()
