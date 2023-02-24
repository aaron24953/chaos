import pygame, time
from math import pi as PI

OG = 0.000001 # 0.01 at 50upf for image

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode(SIZE)
traceRect = pygame.Surface(SIZE)
UPF = 500
G = OG/UPF
NATLENGTH = 100

class Spring():
    def __init__(self, length: float = 2, constant: float = 1):
        self.CONSTANT = constant * G
        self.length = length * NATLENGTH
        self.vel = 0

    def update(self):
        extension = self.length / NATLENGTH - 1
        self.vel += - G - extension * self.CONSTANT
        self.length += self.vel


class Ball():
    def __init__(self, height: float):
        self.height = height
        self.vel = 0

    def update(self):
        self.vel += -G
        self.height += self.vel



def displayOneVsOne():
    # leng = 1.42319  # 1.42319
    spring = Spring((1 - 8/ (PI ** 2 + 4)) + 1, (PI ** 2 + 4)/4)  # 1.43, 3.45
    ball = Ball(spring.length + 0.000291)
    i = 0
    updating = True
    ACC = 6 # accuracy
    VS = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        i+=1
        screen.fill((0, 0, 0))
        if updating:
            for j in range(UPF):  # type: ignore
                if VS:
                    if spring.length <= 0 and ball.height <= 0:
                        print("tie")
                        updating = False
                        break
                    elif spring.length <= 0:
                        print("spring win")
                        updating = False
                        break
                    elif ball.height <= 0:
                        print("ball win")
                        updating = False
                        break

                springG = (spring.length / NATLENGTH - 1) * spring.CONSTANT
                spring.update()
                ball.update()
                pygame.draw.circle(traceRect, (0, 0, 255), (i, HEIGHT/2 - ball.height), 1)
                pygame.draw.circle(traceRect, (255, 0, 255), (i, HEIGHT/2 - spring.length), 1)
                pygame.draw.circle(traceRect, (0, 255, 255), (i, HEIGHT/2 - ball.vel / G / UPF / 5), 1)
                pygame.draw.circle(traceRect, (255, 255, 0), (i, HEIGHT/2 - spring.vel / G / UPF / 5), 1)
                pygame.draw.circle(traceRect, (0, 255, 0), (i, HEIGHT/2 + 50), 1)
                pygame.draw.circle(traceRect, (255, 0, 0), (i, HEIGHT/2 + (1 + springG / G) * 50), 1)
        screen.blit(traceRect, (0, 0))
        pygame.draw.line(screen, (255, 255, 255), (WIDTH*2//3, HEIGHT/2), (WIDTH*2//3, HEIGHT/2 - spring.length))
        pygame.draw.line(screen, (127, 127, 127), (0,HEIGHT/2), (WIDTH, HEIGHT/2))
        pygame.draw.circle(screen, (255, 255, 255), (WIDTH//3, HEIGHT/2 - ball.height), 1)
        screen.blit(font.render(f"Velocity: {round(ball.vel, ACC)}", False, (255, 255, 255)), (0, 0))
        screen.blit(font.render(f"Height: {round(ball.height, ACC)}", False, (255, 255, 255)), (0, 30))
        screen.blit(font.render(f"Velocity: {round(spring.vel, ACC)}", False, (255, 255, 255)), (0, 60))
        screen.blit(font.render(f"Height: {round(spring.length, ACC)}", False, (255, 255, 255)), (0, 90))
        clock.tick(30)
        pygame.display.flip()
        if i == WIDTH:
            updating = False


def testVsForRange():
    LENGDIVISION = 0.01
    CONSDIVISION = 0.01
    colour = (255, 255, 255)

    start = time.time()

    for i in range(int(1/LENGDIVISION), 2 * int(1/LENGDIVISION)):
        ball = Ball(i * NATLENGTH * LENGDIVISION)
        t = 0
        while ball.height > 0:
            t += 1
            ball.update()

        bTime = t
        for j in range(0, int(10/CONSDIVISION)):
            spring = Spring(i*LENGDIVISION, j*CONSDIVISION)
            noWin = True
            t = 0
            while noWin:
                t += 1
                spring.update()
                if spring.length <= 0:
                    noWin = False
                elif bTime < t:
                    noWin = False
                    colour = (0, 0, 255)

            if t == bTime:
                colour = (255, 0, 255)
            elif t <= bTime:
                colour = (255, 0, 0)
            elif bTime < t:
                colour = (0, 0, 255)

            pygame.draw.circle(traceRect, colour, (j + 100, i), 1)
        print(i - int(1/LENGDIVISION),end="\r")

    end = time.time()
    print(end - start)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(traceRect, (0, 0))
        clock.tick(30)
        pygame.display.flip()



def testVsForArea():
    LENGDIVISION = 0.00001
    colour = (255, 255, 255)

    start = time.time()
    startVal = 1.42319

    for i in range(0, 100):
        ball = Ball(NATLENGTH * (i * LENGDIVISION + startVal))
        spring = Spring(i*LENGDIVISION + startVal, PI ** 2 / 2 / (i * LENGDIVISION + startVal))
        noWin = True
        while noWin:
            spring.update()
            ball.update()
            if spring.length <= 0 and ball.height <= 0:
                noWin = False
                print("tie:", i * LENGDIVISION + startVal)
            elif spring.length <= 0:
                print("spring:", i * LENGDIVISION + startVal)
                noWin = False
            elif ball.height <= 0:
                print("ball:", i * LENGDIVISION + startVal)
                noWin = False


            # pygame.draw.circle(traceRect, colour, (0, i), 1)

    end = time.time()
    print(end - start)

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             exit()

    #     screen.blit(traceRect, (0, 0))
    #     clock.tick(30)
    #     pygame.display.flip()

# testVsForRange()
displayOneVsOne()
# testVsForArea()
