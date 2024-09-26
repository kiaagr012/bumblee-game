import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

bee = Actor('bee.png')
posb = pos('bee.png')

flower = Actor('flower.png')
posf = pos('flower.png')

def draw():
    screen.blit('background', (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text('score : '+ str(score), color = 'red', topleft = (10,10))

pgzrun()
