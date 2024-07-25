from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class SNAKE:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(position)
        self.snake.append(tim)

    def extend(self):
        self.add_body(self.snake[-1].position())

    def move_snake(self):
        for num in range(len(self.snake) - 1, 0, -1):
            x_cord = self.snake[num - 1].xcor()
            y_cord = self.snake[num - 1].ycor()
            self.snake[num].goto(x=x_cord, y=y_cord)
        self.snake[0].forward(20)

    def self_collision(self):
        for segment in self.snake[1:]:
            if self.snake_head.distance(segment) < 10:
                return True
        return False

    def snake_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def snake_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def snake_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def snake_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
