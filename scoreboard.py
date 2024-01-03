from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 22, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.score_calc()

    def score_calc(self):
        self.clear()
        self.score += 1
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score} High score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = -1
        self.score_calc()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!!", align=ALIGN, font=FONT)
