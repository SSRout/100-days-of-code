from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_Forwards():
    tim.forward(10)

def move_Backwards():
    tim.backward(10)

def move_Left():
    new_head=tim.heading()+10
    tim.setheading(new_head)

def move_Right():
    new_head=tim.heading()-10
    tim.setheading(new_head)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_Forwards,"w")
screen.onkey(move_Backwards,"s")
screen.onkey(move_Left,"a")
screen.onkey(move_Right,"d")
screen.onkey(clear,"c")
screen.exitonclick()
