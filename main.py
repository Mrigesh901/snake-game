from snakeClass import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenia")
screen.tracer(0)
# turn off the turtle animation
game_is_on = True
snake = Snake()
food = Food()
sb = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.increase_score()
        sb.updt()
        snake.extend()

    # detect collisions with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        # game_is_on = False
        sb.reset()
        snake.reset()

    # detect collisions with the own segments of snake
    new_snake = snake.segments[1:]
    for segment in new_snake:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            sb.reset()
            snake.reset()


screen.exitonclick()
