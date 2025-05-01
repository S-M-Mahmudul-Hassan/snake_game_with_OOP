# imported turtle module
import turtle

# Defined global variable tuple STARTING_POSITION for initial snake segments creation
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# Defined global variable MOVE DISTANCE for snake move
MOVE_DISTANCE = 20
# All 4 direction move setheading variables defined
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Snake class created
class Snake:
    """This Snake class creates snake object segments. This class defines methods for how the snake moves, how it
    resets when hits a wall or its tail and how it extends when eats food."""

    # attributes to create snake object:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # method to create snake segments
    def create_snake(self):
        """Method to create snake segments initially"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    # Method to create each snake segments
    def add_segment(self, seg):
        """Method to create every snake segment object and append to the empty segments[] list"""
        new_segment = turtle.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(seg)
        self.segments.append(new_segment)

    # Method to reset screen when the snake hits the wall or its tail
    def reset(self):
        """Method to reset the game screen once the snake hit tail or wall."""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Method to extend snake segments
    def extend(self):
        """Method to extend segments once snake eats food."""
        self.add_segment(self.segments[-1].position())

    # Method to move each snake segments
    def move(self):
        """Method for snake segments to move forward. The last segment moves first to the position of the
        second to last segment and then the second to last segment moved to the position of the previous
        segment and so on up to the head movement. All segments follow the head movement position."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Method to move up
    def up(self):
        """Method to move up when heading is not down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Method to move down
    def down(self):
        """Method to move down when heading is not up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Method to move left
    def left(self):
        """Method to left down when heading is not right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Method to move right
    def right(self):
        """Method to move right when heading is not left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
