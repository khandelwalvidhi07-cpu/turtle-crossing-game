import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
turtle = Player()
screen.onkey(turtle.up, "Up")

score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move()

    if random.randint(0, 10)%5 == 0:
        car_manager.new_car()

    if turtle.refresh():
        score_board.increase_score()
        car_manager.increase_speed()

    #Detecting collide
    for car in car_manager.cars:
        if car.xcor()-25 < turtle.xcor() < car.xcor()+25 and turtle.distance(car) < 30:
            score_board.game_over()
            game_is_on = False
        elif car.ycor()-20 < turtle.ycor() < car.ycor()+20 and turtle.distance(car) < 15 :
            score_board.game_over()
            game_is_on = False

    screen.update()

screen.exitonclick()