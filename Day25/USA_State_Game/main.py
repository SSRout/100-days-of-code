import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S State Games")
image="Day25/USA_State_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("Day25/USA_State_Game/50_states.csv")
all_states=data.state.tolist()
guess_state=[]
while len(guess_state)<3:
    answer_state=screen.textinput(title=f"{len(guess_state)}/50 Corrected",prompt="Sate Name?").title()
    guess_state.append(answer_state)
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        res=data[data.state==answer_state]
        t.goto(int(res.x),int(res.y))
        t.color("red")
        t.write(answer_state)
screen.exitonclick()