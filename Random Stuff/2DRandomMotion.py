from random import random
import pygame

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

MOVEINC = 1
size = width, height = 1600, 900
screen = pygame.display.set_mode(size)
traceRect = pygame.Surface(size)
font = pygame.font.SysFont("Arial", 30)

a = [[width/2, height/2],(0,0)]
i=0
c=[]
UPF = 10001

def rainbow(x: float):
    x = x % (255 * 6)
    if x <= 255:
        col = (255, x, 0)
    elif x <= 2 * 255:
        col = (255 * 2 - x, 255, 0)
    elif x <= 3 * 255:
        col = (0, 255, x - 2 * 255)
    elif x <= 4 * 255:
        col = (0, 4 * 255 - x, 255)
    elif x <= 5 * 255:
        col = (x - 4 * 255, 0, 255)
    else:
        col = (255, 0, 255 * 6 - x)
    return col


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for j in range(UPF):
        i+=1
        a[1] = (a[0][0], a[0][1])
        r=random()
        if r<0.25:
            a[0][0]+=MOVEINC
        elif r<0.5:
            a[0][0]-=MOVEINC
        elif r<0.75:
            a[0][1]+=MOVEINC
        else:
            a[0][1]-=MOVEINC
        if a[0] == [width/2, height/2]: c.append(i)
        pygame.draw.line(traceRect, rainbow((i/UPF)//5), a[0], a[1], 1)
    screen.fill((0, 0, 0))
    screen.blit(traceRect, (0, 0))
    screen.blit(font.render(f"Iterations: {i}", True, (255, 255, 255),(0, 0, 0)), (0, 0))
    screen.blit(font.render(f"Cords: {a[0]}", True, (255, 255, 255),(0, 0, 0)), (0, 30))
    screen.blit(font.render(f"Centres: {c}", True, (255, 255, 255),(0, 0, 0)), (0, 60))
    pygame.display.flip()
