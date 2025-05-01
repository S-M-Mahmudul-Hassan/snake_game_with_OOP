# imported Turtle class from turtle module.
from turtle import Turtle
# imported random module
import random


class Food(Turtle):
    """This class creates food objects. It also defines method to recreate foods once eaten by the snake."""

    # Attributes to create food object.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # Method to recreate the food.
    def refresh(self):
        """Method to recreate the food randomly once the previous food is eaten by the snake."""
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
