# Imported Turtle class from turtle module.
from turtle import Turtle

# Created global variables ALIGN and FONT for the use in write method.
ALIGN = 'center'
FONT = ('Courier', 20, 'normal')

# Created score_turtle object from Turtle class.
score_turtle = Turtle()


class Scoreboard(Turtle):
    """this class creates the scoreboard object. It also updates the scoreboard, reset, game over and
    increases the scores."""

    # Attributes for the scoreboard object
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("snake_high_score_keeper.txt") as content:
            self.high_score = int(content.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    # Method to update the scoreboard with clearing the screen.
    def update_scoreboard(self):
        """Method to update the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score}    High Score:{self.high_score}", align=ALIGN, font=FONT)

    # Method to reset the scoreboard with high score once the current score increases more than previous high score.
    def reset(self):
        """Method to reset high score."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_high_score_keeper.txt", mode="w") as content:
                content.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # Method that increases the score once the snake eats a food.
    def increase_score(self):
        """Method to increase the score."""
        self.score += 1
        self.update_scoreboard()
