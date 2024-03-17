from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.speed(0)
        self.clear()
        self.goto(-200, 220)
        self.write(f"Level: {self.level}", align='center', font=('Arial', 16, 'normal')) 

    def increase_level(self):
        self.level += 1
        self.update_level()
        

