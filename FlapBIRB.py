import pygame as pg
import time
import random
import keyboard

pg.init()
pg.font.init()
pg.font.get_init()

screen = pg.display.set_mode((1200,800))
green = (0,200,100)
lblue = (0,210,255)
orange = (255, 165, 0)
pipeup = [1100, 0, 100, random.randint(100,400)]
pipedown = [1100, pipeup[3] + 200, 100, 800 - pipeup[1]]

pipedown2 = [500, 600, 100, 200]
pipeup2 = [500, 0, 100, 400]
BIRB = [200, 380, 50, 50]
BIRBgrav = 0
clickcooldown = 0
grav = 0

score = 0


scorefont = pg.font.SysFont('freesanbol.ttf', 100)


while True:




    screen.fill(lblue)
    pg.draw.rect(screen, green, pipedown)
    pg.draw.rect(screen, green, pipeup)
    pg.draw.rect(screen, green, pipedown2)
    pg.draw.rect(screen, green, pipeup2)

    pg.draw.rect(screen, green, (pipeup[0] - 25, pipeup[1] + pipeup[3] - 50, 150, 100))
    pg.draw.rect(screen, green, (pipeup2[0] - 25, pipeup2[1] + pipeup2[3] - 50, 150, 100))
    pg.draw.rect(screen, green, (pipeup2[0] - 25, pipeup2[1] + pipeup2[3] + 200, 150, 100))
    pg.draw.rect(screen, green, (pipeup[0] - 25, pipeup[1] + pipeup[3] +200, 150, 100))

    pg.draw.ellipse(screen, orange, BIRB)

    scoretext = scorefont.render('Score = ' + str(score), True, (0,255,0))
    textRect = scoretext.get_rect()
    textRect.center = (600,100)
    screen.blit(scoretext, textRect)


    pipedown[0] -= 5
    pipeup[0] -= 5
    pipedown2[0] -= 5
    pipeup2[0] -= 5

    if keyboard.is_pressed('SPACE') and clickcooldown <= 0:
        BIRBgrav += 100
        clickcooldown = 10
        grav = 0

    if BIRBgrav <= 0:
        BIRB[1] += 10 * grav
    else:
        BIRB[1] -= 10
        BIRBgrav -= 25

    if BIRB[1] >= 750:
        BIRB[1] = 750

    clickcooldown -= 1
    grav += 0.0125


    if pipeup[0] == -110:
        pipeup[0] = 1200
        pipedown[0] = 1200
        pipeup[3] = random.randint(100,400)
        pipedown[1] = pipeup[3] + 200
        pipedown[3] = 800 - pipeup[1]
        score += 1
        print(score)

    if pipeup2[0] == -110:
        pipeup2[0] = 1200
        pipedown2[0] = 1200
        pipeup2[3] = random.randint(100,400)
        pipedown2[1] = pipeup2[3] + 200
        pipedown2[3] = 800 - pipeup2[1]
        score += 1
        print(score)

    if BIRB.collideRect(pipeup2):
        stop()

    time.sleep(0.01)
    pg.display.flip()
