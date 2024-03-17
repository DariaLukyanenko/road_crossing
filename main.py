from turtle import Screen
from player import Player
from score import Score
from cars import Cars
from time import sleep
from random import randint

# TODO 1 Черепаха коснулась верха экрана, но она должна появится снизу и lvl должен поменяться ✔️
# TODO 2 Сделать логику машины ✔️
# TODO 3 Логика столкновения с машинами / сбития игрока ✔️
# TODO 4 Сделать множество машин повторяющие шаги 2 и 3 ✔️
# TODO 5 Улучшить появление машиин ✔️

WIDTH, HEIGHT = 500, 500

screen = Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor('white')

cars = Cars()
player = Player()
score = Score()

screen.listen()
screen.onkey(player.move,'w')

def game():
    game_going = True
    time=2
    while game_going:
        sleep(1/time)
        print(1/time)
        screen.update()
        cars.move()

        random_chance = randint(1,3)
        if random_chance == 2:
            cars.createcar()

        if player.ycor() > HEIGHT/2:
            player.setpos(0,-230)
            score.increase_level()
            time *= 2


        for car in cars.list:
            if player.distance(car) < 25:
                game_going=False
                return

game()


screen.exitonclick()