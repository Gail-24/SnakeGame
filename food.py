import random
from turtle import Turtle


class FOOD(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        loc_x = random.randint(-280, 280)
        loc_y = random.randint(-280, 280)
        self.goto(x=loc_x, y=loc_y)
