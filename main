from turtle import Screen
import time
from snake import SNAKE
from food import FOOD
from scoreboard import SCOREBOARD

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = SNAKE()
my_food = FOOD()
my_score = SCOREBOARD()
my_score.display()


screen.listen()
screen.onkey(key="Right", fun=my_snake.snake_right)
screen.onkey(key="Up", fun=my_snake.snake_up)
screen.onkey(key="Left", fun=my_snake.snake_left)
screen.onkey(key="Down", fun=my_snake.snake_down)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move_snake()

# detect collision with food
    if my_snake.snake_head.distance(my_food) < 15:
        my_food.refresh()
        my_score.refresh()
        my_snake.extend()

    if (my_snake.snake_head.xcor() > 300 or my_snake.snake_head.xcor() < -300 or my_snake.snake_head.ycor() > 300 or
            my_snake.snake_head.ycor() < -300):
        game_on = False
        my_score.game_over()

    if my_snake.self_collision():
        game_on = False
        my_score.game_over()

screen.exitonclick()
