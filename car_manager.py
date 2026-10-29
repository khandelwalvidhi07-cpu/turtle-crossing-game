from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


def create():
    car = Turtle()
    car.shape("square")
    car.shapesize(stretch_len=2, stretch_wid=1)
    car.color(random.choice(COLORS))
    car.penup()
    return car

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.cars = []
        self.multiple_cars()

    def multiple_cars(self):
        for num in range(20):
            car = create()
            x_cor = random.randint(-300,300)
            y_cor = random.randint(-270, 300)
            car.setposition(x_cor, y_cor)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.setx(car.xcor() - self.speed)

    def new_car(self):
        car = create()
        y_cor = random.randint(-260, 300)
        car.setposition(290, y_cor)
        self.cars.append(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT