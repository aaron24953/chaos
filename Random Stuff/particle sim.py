from random import random
import pygame
import math

pygame.init()
pygame.font.init()


class particle:
    def __init__(
        self,
        x=0,
        y=0,
        xv=0,
        yv=0,
        mass=225,
        colour=(255, 255, 255),
        TBC=0,
        hasG=False,
        state=-1,
    ):
        self.vel = [xv, yv]
        self.pos = [x, y]
        self.mass = mass
        self.size = math.sqrt(mass)
        self.hasG = hasG
        self.collided = 0
        self.colour = colour
        self.TBC = TBC
        self.state = state

    def update(self, w, h, UPS):
        g = 0.5 / UPS
        if self.hasG:
            self.vel[1] += g
        if not 0 + 2 * math.sqrt(self.mass) <= self.pos[0] + math.sqrt(self.mass) <= w:
            self.vel[0] = -self.vel[0]
        if not 0 + 2 * math.sqrt(self.mass) <= self.pos[1] + math.sqrt(self.mass) <= h:
            self.vel[1] = -self.vel[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.state == 0:
            self.vel[0] *= 1 - 0.1 / UPS
            self.vel[1] *= 1 - 0.1 / UPS
        if self.state == 1:
            self.vel[0] *= 1 / (1 - (0.1 / UPS)) + 1 / UPS**2
            self.vel[1] *= 1 / (1 - (0.1 / UPS)) + 1 / UPS**2

    def launch(self, ang, vel, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.vel[0] = math.cos(ang) * vel
        self.vel[1] = math.sin(ang) * vel
        pass


def distBetween(a, b):
    return math.sqrt((a.pos[0] - b.pos[0]) ** 2 + (a.pos[1] - b.pos[1]) ** 2)


def collide(a, b, uNum):
    PI = math.pi
    av = math.sqrt(a.vel[0] ** 2 + a.vel[1] ** 2)
    bv = math.sqrt(b.vel[0] ** 2 + b.vel[1] ** 2)
    ahv = a.vel[0]
    bhv = b.vel[0]
    avv = a.vel[1]
    bvv = b.vel[1]
    if av == 0:
        aa = PI / 2
    else:
        aa = math.asin(avv / av)
    if ahv < 0:
        aa = PI - aa
    if bv == 0:
        ba = PI / 2
    else:
        ba = math.asin(bvv / bv)
    if bhv < 0:
        ba = PI - ba
    if a.pos[0] == b.pos[0]:
        ca = PI / 2
    else:
        ca = math.atan((a.pos[1] - b.pos[1]) / (a.pos[0] - b.pos[0]))
    a.vel[0] = (
        av * math.cos(aa - ca) * (a.mass - b.mass) + 2 * b.mass * bv * math.cos(ba - ca)
    ) / (a.mass + b.mass) * math.cos(ca) + av * math.sin(aa - ca) * math.cos(
        ca + PI / 2
    )
    a.vel[1] = (
        av * math.cos(aa - ca) * (a.mass - b.mass) + 2 * b.mass * bv * math.cos(ba - ca)
    ) / (a.mass + b.mass) * math.sin(ca) + av * math.sin(aa - ca) * math.sin(
        ca + PI / 2
    )
    b.vel[0] = (
        bv * math.cos(ba - ca) * (b.mass - a.mass) + 2 * a.mass * av * math.cos(aa - ca)
    ) / (b.mass + a.mass) * math.cos(ca) + bv * math.sin(ba - ca) * math.cos(
        ca + PI / 2
    )
    b.vel[1] = (
        bv * math.cos(ba - ca) * (b.mass - a.mass) + 2 * a.mass * av * math.cos(aa - ca)
    ) / (b.mass + a.mass) * math.sin(ca) + bv * math.sin(ba - ca) * math.sin(
        ca + PI / 2
    )
    a.collided = uNum
    b.collided = uNum


def rGen(h, w, PI, UPS, g, vel=400):
    p = particle(
        xv=2 * vel / UPS * (random() - 0.5),
        yv=2 * vel / UPS * (random() - 0.5),
        y=h * random(),
        x=w * random(),
        mass=(random() ** (1 / 2)) * 300,
    )
    if g:
        p.hasG = True
    return p


def rLaunch(h, PI):
    p = particle(h)
    p.launch(random() * (PI / 3) + PI / 12, random() * 3 + 2, (0, h))
    return p


def rAngLaunch(v, h, PI):
    p = particle(h)
    p.launch(random() * (PI / 2), v, (0, h))
    return p


def createWall(pa, n, h, g, v, UPS):
    for i in range(n):
        p = particle(mass=16)
        p.hasG = False
        p.launch(math.pi / 2 * i / n, v, (0 + p.size, h - p.size))
        p.TBC = 2 * UPS
        pa.append(p)
    return pa


def removeBad(particles, w, h):
    noPurged = 0
    toPop = []
    for i in range(len(particles)):
        inWall = False
        a = particles[i]
        if not 0 + 2 * a.size <= a.pos[0] + a.size <= w:
            inWall = True
        if not 0 + 2 * a.size <= a.pos[1] + a.size <= h:
            inWall = True
        for j in range(i + 1, len(particles)):
            if inWall:
                toPop.append(i)
                noPurged += 1
                break
            b = particles[j]
            dist = distBetween(a, b)
            if dist < a.size + b.size:
                toPop.append(i)
                noPurged += 1
                break
    toPop = toPop[::-1]
    for i in toPop:
        particles.pop(i)
    noPinkPurge = False
    for part in particles:
        if part.colour == (255, 0, 255):
            noPinkPurge = True
    if not noPinkPurge:
        particles[0].colour = (255, 0, 255)
    print(noPurged, len(particles))


def getEk(particles):
    Ek = 0
    for part in particles:
        v = math.sqrt(part.vel[0] ** 2 + part.vel[1] ** 2)
        m = part.mass
        Ek += 0.5 * m * v**2
    return Ek


def main():
    font = pygame.font.SysFont("Arial", 30)
    FPS = 60
    UPF = 10
    uNum = 0
    cDelay = -1
    UPS = FPS * UPF
    PI = math.pi
    bgCol = (25, 25, 25)
    w = 800
    h = 450
    screen = pygame.display.set_mode((w, h))
    running = True
    particles = []
    # particles.append(particle(y=h-200,x=200,colour=(255,0,255)))
    for i in range(50):
        particles.append(rGen(h, w, PI, UPS, False))
    # for i in range(len(particles),len(particles)+0):#not fps based
    #  particles.append(rLaunch(h,PI))
    # for i in range(len(particles),len(particles)+0):
    #  particles.append(rAngLaunch(50/FPS,h,PI))
    removeBad(particles, w, h)
    # particles=createWall(particles,50,h,False,200/UPS,UPS)
    while running:
        screen.fill(bgCol)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(UPF):
            uNum += 1
            for i in range(len(particles)):
                a = particles[i]
                for j in range(i + 1, len(particles)):
                    b = particles[j]
                    dist = distBetween(a, b)
                    if a.TBC < uNum and b.TBC < uNum:
                        if a.collided + cDelay < uNum and b.collided + cDelay < uNum:
                            if dist < a.size + b.size:
                                collide(a, b, uNum)
                a.update(w, h, UPS)
        if uNum % (20 * UPS) == 0:
            for part in particles:
                part.state = (part.state + 1) % 2
                if part.state:
                    part.colour = (255, 200, 200)
                    bgCol = (50, 25, 25)
                else:
                    part.colour = (200, 200, 255)
                    bgCol = (25, 25, 50)
            removeBad(particles, w, h)
        for part in particles:
            pygame.draw.circle(
                screen,
                part.colour,
                (int(part.pos[0]), int(part.pos[1])),
                int(math.sqrt(part.mass)),
            )
        screen.blit(
            font.render(
                "E\u2096:" + str(round(getEk(particles))), False, (255, 255, 255)
            ),
            (0, 0),
        )
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
