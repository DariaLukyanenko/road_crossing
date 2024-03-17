from turtle import Turtle

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.goto(0,-230)
        self.setheading(90)
        
    def move(self):
        self.fd(20)
        