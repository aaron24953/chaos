# better champs

import random
import pygame

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
traceRect = pygame.Surface(size)
font = pygame.font.SysFont("Arial", 100)

file = open("message.txt", "r")
text = file.readlines()
names = []
for i in range(0, len(text), 2):
    names.append(text[i][1:-1])

numChamps = len(names)
stats = [[0, 0] for i in range(numChamps)]

matchups = []
for i in range(numChamps):
    for j in range(i + 1, numChamps):
        matchups.append((i, j))

matchup = random.choice(matchups)
matchups.remove(matchup)

finished = False
limit = 1000

i = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not finished:
            pos = pygame.mouse.get_pos()
            if pos[0] <= width // 2:
                stats[matchup[0]][0] += 1
                stats[matchup[1]][1] += 1
            else:
                stats[matchup[0]][1] += 1
                stats[matchup[1]][0] += 1
            if matchups and not finished and i < limit:
                i += 1
                matchup = random.choice(matchups)
                matchups.remove(matchup)
            else:
                finished = True
                ratios = [
                    (stats[j][0] / (stats[j][0] + stats[j][1]), j)
                    for j in range(len(stats))
                ]
                ratios.sort(reverse=True)
                file = open("results.txt", "w")
                for ratio in ratios:
                    file.write(f"{names[ratio[1]]}: {ratio[0]}\n")
                file.close()
    screen.fill((0, 0, 0))
    if not finished:
        screen.blit(font.render(f"{i}", True, (255, 255, 255), (0, 0, 0)), (0, 0))
        name = font.render(f"{names[matchup[0]]}", True, (255, 255, 255), (0, 0, 0))
        rect = name.get_rect(center=(width // 4, height // 2))
        screen.blit(name, rect)
        name = font.render(f"{names[matchup[1]]}", True, (255, 255, 255), (0, 0, 0))
        rect = name.get_rect(center=(width * 3 // 4, height // 2))
        screen.blit(name, rect)
        pygame.draw.line(
            screen, (255, 255, 255), (width // 2, 0), (width // 2, height), 5
        )
    else:
        title = font.render("Winrates", True, (255, 255, 255), (0, 0, 0))
        rect = title.get_rect(center=(width // 2, 60))
        screen.blit(title, rect)
        for i in range(5):
            screen.blit(
                font.render(
                    f"{names[ratios[i][1]]}: {round((ratios[i][0]* 100))}% ",
                    True,
                    (255, 255, 255),
                    (0, 0, 0),
                ),
                (0, 120 * (i + 1)),
            )
            screen.blit(
                font.render(
                    f"{names[ratios[-(i+1)][1]]}: {round((ratios[-(i+1)][0]* 100))}% ",
                    True,
                    (255, 255, 255),
                    (0, 0, 0),
                ),
                (width // 2, 120 * (i + 1)),
            )
    pygame.display.flip()
