import turtle as t
import random
timmy=t.Turtle()
timmy.pensize(15)
colors=["CornFlowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
direction=[0,90,180,270]
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen=t.Screen()
screen.exitonclick()