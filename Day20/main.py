from turtle import Screen
from food import Food
from snake import Snake
from score import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Ninja")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True

while game_on:
    screen.update()
    time.sleep(1)
    snake.move()  
    #detect food collision
    if snake.head.distance(food)<15:
        score.increase_score()
        food.refresh()

    #detect wall collision
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        score.game_over()

screen.exitonclick()
