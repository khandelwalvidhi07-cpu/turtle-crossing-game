from turtle import Turtle

FONT = ("Courier", 17, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.setposition(-290, 280)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER.", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)