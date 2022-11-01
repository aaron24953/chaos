import pygame as p
from sys import *
from math import sin, cos

lines = True
trace = True
tEveryF = True
rain = True
rainRate = 0.1  # 0.541
numRainCycles = 100
PI = 3.1415926535897932384624338327950288419716939937510582

p.init()

clock = p.time.Clock()

size = width, height = 800, 450
black = 0, 0, 0
FPS = 0
UPF = 40
center = (width / 2, height / 2)
screen = p.display.set_mode(size)
traceRect = p.Surface(size)
numU = 0

rad = 1
penCol = (255, 0, 255)
traceCol = (255, 0, 0)
# [vel,ang,mass,len]
a = [0.00004, PI, 2, 150]
b = [0.0005, PI, 1, 250]
g = 0.0001


def rainbow(x):
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


def update():
    global numU
    numU += 1
    v1 = a[0]
    v2 = b[0]
    t1 = a[1]
    t2 = b[1]
    m1 = a[2]
    m2 = b[2]
    l1 = a[3]
    l2 = b[3]
    a[0] += (
        -g * (2 * m1 + m2) * sin(t1)
        - m2 * g * sin(t1 - 2 * t2)
        - 2 * sin(t1 - t2) * m2 * (v2 * v2 * l2 + v1 * v1 * l1 * cos(t1 - t2))
    ) / (l1 * (2 * m1 + m2 - m2 * cos(2 * t1 - 2 * t2)))
    b[0] += (
        2
        * sin(t1 - t2)
        * (
            v1 * v1 * l1 * (m1 + m2)
            + g * (m1 + m2) * cos(t1)
            + v2 * v2 * l2 * m2 * cos(t1 - t2)
        )
    ) / (l2 * (2 * m1 + m2 - m2 * cos(2 * t1 - 2 * t2)))
    a[0] *= 1
    b[0] *= 1
    a[1] += a[0]
    b[1] += b[0]


while numU < (255 * 6 * UPF / rainRate) * numRainCycles:
    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
    update()
    screen.fill(black)
    posa = (a[3] * sin(a[1] + PI) + center[0], -a[3] * cos(a[1] + PI) + center[1])
    posb = (posa[0] + b[3] * sin(b[1] + PI), posa[1] - b[3] * cos(b[1] + PI))
    if rain:
        penCol, traceCol = rainbow((numU // UPF) // (1 / rainRate)), rainbow(
            (numU // UPF) // (1 / rainRate)
        )
    if trace and tEveryF:
        p.draw.circle(traceRect, traceCol, (int(posb[0]), int(posb[1])), rad)
    if numU % UPF == 0:
        p.draw.circle(traceRect, traceCol, (int(posb[0]), int(posb[1])), rad)
        if trace:
            screen.blit(traceRect, (0, 0))
        if lines:
            p.draw.lines(screen, penCol, False, (center, posa, posb), 10)
        p.display.flip()
        clock.tick(FPS)
