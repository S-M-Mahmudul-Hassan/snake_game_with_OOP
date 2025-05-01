# turtle module imported
import turtle
# imported Snake class from snake module
from snake import Snake
# imported Food class from food module
from food import Food
# imported Scoreboard class from snake_game_scoreboard module
from snake_game_scoreboard import Scoreboard
# imported time module
import time

# Created screen object from Screen class
screen = turtle.Screen()
# created screen window size using setup method from object
screen.setup(width=600, height=600)
# created screen background color to black using bgcolor method
screen.bgcolor("black")
# written title of the game
screen.title("Snake Game")
# Stopped the animation of the object with tracer method. The screen is updated later in while loop with 0.1 sec sleep
screen.tracer(0)

# snake object is created from Snake class
snake = Snake()
# food object is created from Food class
food = Food()
# scoreboard object is created from Scoreboard class
scoreboard = Scoreboard()

# screen is listening for key press. listen() method works continuously without while loop.
screen.listen()
# Two positional arguments are provided for the function and key for onkey method for all 4 directions.
screen.onkey(fun=snake.up, key="Up") 
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
# while loop is created for the game play.
while game_is_on:
    # screen is updated from the tracer (animation stop) method.
    screen.update()
    # screen is made to sleep for 0.1 seconds for the snake to move without flickering.
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Game over due to wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # for loop is created starting after the head segment to check the snake hitting tail condition.
    for segment in snake.segments[1:]:  # To skip the distance from head to head because the iteration will start with head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
