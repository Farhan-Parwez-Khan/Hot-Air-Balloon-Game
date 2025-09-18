# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:43:40 2025

@author: FARHAN PARWEZ KHAN
"""

import pygame as pg
import random as ra

pg.font.init()
screen = pg.display.set_mode((1530, 800))
pg.display.set_caption("HOT AIR BALLOON GAME")

h = pg.image.load("D:\Farhan\Py2\Balloon.png")
bu = pg.image.load("D:\Farhan\Py2\Bubble.png")
kc = pg.image.load("D:\Farhan\Py2\kanta.png")
font = pg.font.SysFont('Comic Sans MS', 30)
font1 = pg.font.SysFont('Comic Sans MS', 44)

hs=[0]
bgc=(255, 255, 255)
runn=True
screen.fill((255, 255, 255))
mtext=font1.render('PRESS LEFT OR RIGHT KEY TO MAKE THE HOT AIR BALLOON MOVE', True, (0, 0, 0))
screen.blit(mtext, (15, 300))
mtext1=font.render('PRESS SPACEBAR TO CONTINUE', True, (0, 0, 0))
screen.blit(mtext1, (475, 400))

xa=750
ya=600

while runn:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                runn=False
                screen.fill((255, 255, 255))
        if event.type == pg.QUIT:
            pg.quit()            
    pg.display.flip()
screen.fill((255, 255, 255))

while 1:

    spj=0
    spjmax=42
    bubpos=[]
    ppos=[]
    
    bgc=(255, 255, 255)

    count = 0
    clock = pg.time.Clock()
    screen.fill(bgc)
    running = True
    score = 0
    x=10
    xa=750
    pr=screen.blit(h, [xa,ya])
    z=1
    
    while running:
        
        if count%10==0:
            a = ra.randint(0,1550)
            b = ra.randint(-1500, 0)
            screen.blit(bu, [a, b])
            bubpos.append([a, b])

        if count%200==0:
            a0 = ra.randint(0,1400)
            b0 = ra.randint(-300, 0)
            screen.blit(kc, [a0,b0])
            ppos.append([a0,b0])
            
        screen.fill(bgc)
        count = count + 1
        
        if count%10==0:
            score +=1
        font = pg.font.SysFont('Comic Sans MS', 30)
        
        if spj == 0 or spj > spjmax-1:
            for i in pg.event.get():
                keys=pg.key.get_pressed()
                if i.type == pg.QUIT:
                    pg.quit()
                if keys[pg.K_LEFT]:
                    xa=xa-50
                if keys[pg.K_RIGHT]:
                    xa=xa+50
                        
        pr=screen.blit(h, [xa,ya])
        
        c=0

        for l in bubpos:
            bubpos[c][1]+=z
            t1=bubpos[c]
            bub=screen.blit(bu, t1)
            c+=1
            if pr.colliderect(bub):
                h = pg.image.load("D:\Farhan\Py2\Balloon.png")
                bubpos.pop(c-1)
                score=score+10
                
        c=0
        
        for p in ppos:
            ppos[c][1]+=z
            t2=ppos[c]
            er=screen.blit(kc, t2)
            c+=1
            if pr.colliderect(er):
                h = pg.image.load("D:\Farhan\Py2\Balloon.png")
                ppos.pop(c-1)
                running=False
        
        if score%20==0:
            z=z+0.1
        
        text = font.render('SCORE: ' + str(score), True, (50, 50, 50))
        texths = font.render('HIGHEST SCORE: ' + str(max(hs)), True, (50 ,50 ,50))
        
        screen.blit(text, (1350,80))
        screen.blit(texths, (1000,80))
        hs.append(score)
        pg.display.flip()
        clock.tick(60)
        