import pygame as p
from sys import *

p.init()

clock=p.time.Clock()

size= width,height = 1600, 900
black=0,0,0
FPS=120

speed=[1,0]
pos=[0,0]
g=0.1

screen=p.display.set_mode(size)

sprite=p.image.load("white square.png")
size=sprite.get_size()

while True:
    for event in p.event.get():
        if event.type == p.QUIT: exit()
    
    pos[0]+=speed[0]
    pos[1]+=speed[1]
    speed[1]+=g
    #speed[1]*=0.99
    
    g+=0.01
    if  pos[1]<0 or pos[1]+size[1]>height:
        speed[1]=-0.9*speed[1]
        pos[1]=height-size[1]
    if  pos[0]< 0 or pos[0]+size[0]>width:
        speed[0]=-speed[0]
    screen.fill(black)
    screen.blit(sprite,pos)
    p.display.flip()
    clock.tick(FPS)