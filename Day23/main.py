import time
from turtle import Screen
from car import Car
from player import Player
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)#stop animation

player=Player()
car_manager=Car()
scoreboard=Score()

screen.listen()
screen.onkey(player.go_up,"Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_on=False
            scoreboard.game_over()
            
    #detect successfull road cross
    if player.is_cross_road():
        player.go_to_begin()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()


