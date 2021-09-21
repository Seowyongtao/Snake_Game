from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()

    def move(self):
        for segment_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            current_body = self.snake_body[segment_num]
            current_body.goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

