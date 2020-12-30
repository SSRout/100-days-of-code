from turtle import Turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            sn=Turtle(shape="square")
            sn.color("red")
            sn.penup()
            sn.goto(pos)
            self.segments.append(sn)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x_cor=self.segments[seg-1].xcor()
            y_cor=self.segments[seg-1].ycor()
            self.segments[seg].goto(x_cor,y_cor)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=180:
             self.head.setheading(0)    

