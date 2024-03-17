from turtle import Turtle
from random import randint

class Cars(Turtle):
    def __init__(self) -> None:
        self.list=[]
        self.createcar()
        
    def createcar(self):
        color_list=["yellow",'red','pink','green','blue']
        car=Turtle()
        car.color(color_list[randint(0,4)])
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.speed(0)
        car.goto(200,randint(-210,210))
        self.list.append(car)
    
    def move(self):
        for car in self.list:
            car.bk(10)





