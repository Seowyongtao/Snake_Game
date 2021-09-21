import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Tao snake game")
screen.tracer(0)

game_on = True
score_board = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.move()
        snake.extend()
        score_board.add_score()
        score_board.refresh()

    # Detect collision with wall
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
