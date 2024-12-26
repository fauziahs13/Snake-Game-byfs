from turtle import Turtle

SQUARE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # TODO 1: Create a snake body
        self.segments_of_snake = []
        self.create_snake()
        self.head = self.segments_of_snake[0]

    def create_snake(self):
        for position in SQUARE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments_of_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.segments_of_snake[-1].position())

    def move(self):
        """Code for figure out a way for the tail of the snake to follow where the head is going"""
        # for seg_num in range(start= 2, stop= 0, step= -1)
        for seg_num in range(len(self.segments_of_snake) - 1, 0, -1):
            new_x = self.segments_of_snake[seg_num - 1].xcor()
            new_y = self.segments_of_snake[seg_num - 1].ycor()
            self.segments_of_snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
