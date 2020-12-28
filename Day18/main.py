from turtle import Turtle,Screen
timmy=Turtle()

timmy.color("green")

timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)

for i in range(1,5):
    timmy.forward(100*i)
    timmy.left(110)

def draw_shape(num_of_sides):
    angle=360/num_of_sides
    for _ in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3,11):
    draw_shape(sides)

screen=Screen()
screen.exitonclick()
