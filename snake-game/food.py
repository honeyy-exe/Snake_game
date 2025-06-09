from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)


    def game_over(self):
        self.pu()
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = FONT)
