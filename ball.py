from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('skyblue')
        self.penup()
        #self.goto(350,350)

    def move(self, x_dir, y_dir):
            new_x = self.xcor() + 10 * x_dir
            new_y = self.ycor() + 10 * y_dir
            self.goto(new_x, new_y)