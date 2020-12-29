from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make Your Bet", prompt='Which turtle will win the race? Enter Color: ')
colors=["red","green","blue","yellow","purple"]
pos=[-70,-40,-10,20,50]
all_turtles=[]
for index in range(0,5):
    tim=Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[index])
    tim.goto(x=-230,y=pos[index])
    all_turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            wining_color=turtle.pencolor()
            if wining_color==user_bet:
                print(f"Bravoo!! {wining_color}")
            else:
                print(f"You Lost! winer is {wining_color}")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
