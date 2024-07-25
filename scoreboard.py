from turtle import Turtle


class SCOREBOARD(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.display()
        self.color("white")

    def display(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", True, "left", ("Arial", 15, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", True, "center", ("Arial", 15, "normal"))

    def refresh(self):
        self.score += 1
        self.display()
