import turtle
from turtle import Turtle
import random
colors = [(37, 191, 134), (76, 95, 141), (33, 126, 70), (191, 162, 26), (106, 105, 203), (142, 7, 147), (185, 35, 158),
          (205, 229, 74), (15, 10, 177), (93, 241, 170), (191, 58, 192), (23, 94, 41), (26, 183, 206), (20, 15, 84),
          (110, 216, 235), (201, 231, 0), (78, 12, 90), (81, 252, 81), (217, 171, 208), (23, 51, 33), (177, 183, 220),
          (42, 77, 79), (97, 103, 14), (3, 5, 254), (0, 249, 254), (202, 188, 187)]
turtle.colormode(255)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.color(random.choice(colors))
        self.goto(random_x, random_y)
