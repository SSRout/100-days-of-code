import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S State Games")
image="Day25/USA_State_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("Day25/USA_State_Game/50_states.csv")
all_states=data.state.tolist()

screen.exitonclick()