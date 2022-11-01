from random import random
import pygame

pygame.init()

clock = pygame.time.Clock()

size = width, height = 1600, 900

FRICTION = 0.99
FPS = 60
P = 0.05
UPF = 1
DV = 5
VMULT = 25

traceRect = pygame.Surface(size)
screen = pygame.display.set_mode(size)
a = [[0, 0], [size[0] / 2, size[1] / 2], [0, 0]]
a[2] = a[1]


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


def update(numI: int):
    for i in range(numI):
        a[2] = (a[1][0], a[1][1])
        if random() < P:
            a[0][0] += (random() - 0.5) * DV + (width / 2 - a[1][0]) / (5 / P)
            a[0][1] += (random() - 0.5) * DV + (height / 2 - a[1][1]) / (5 / P)
        a[0][0] *= FRICTION
        a[0][1] *= FRICTION
        a[1][0] += a[0][0]
        a[1][1] += a[0][1]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.draw.line(
        traceRect,
        rainbow((a[0][0] ** 2 + a[0][1] ** 2) ** (1 / 1.5) * 10),
        a[1],
        a[2],
        3,
    )
    screen.fill((0, 0, 0))
    screen.blit(traceRect, (0, 0))
    pygame.draw.circle(screen, (255, 255, 255), a[1], 5)
    pygame.draw.line(
        screen,
        (255, 255, 0),
        a[1],
        (a[0][0] * VMULT + a[1][0], a[0][1] * VMULT + a[1][1]),
        3,
    )
    pygame.display.flip()
    update(UPF)
    clock.tick(FPS)
