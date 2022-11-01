import random


class Board:
    def __init__(self, size: int):
        self.size = size
        self.spaces = [
            1 if random.random() < 0.3 else 0 for i in range(size**2)  # type: ignore
        ]

    def iterate(self):
        iteration = [p for p in self.spaces]
        s = self.size
        for i in range(self.size**2):
            value = 0
            if 0 < i % s < s - 1 and 0 < i // s < s - 1:
                for move in [-s - 1, -s, 1 - s, -1, 1, s - 1, s, s + 1]:
                    value += self.spaces[i + move]
            elif i == 0:
                for move in [-1, -s, -s + 1, s, s + 1, 1, s - 1, 2 * s - 1]:
                    value += self.spaces[i + move]
            elif i == s - 1:
                for move in [s, -s, 1, -s + 1, -2 * s + 1, -s - 1, -1, s - 1]:
                    value += self.spaces[i + move]
            elif i == s**2 - s:
                for move in [1, -s + 1, s - 1, -s, -1, -i + s - 1, -i, -i + 1]:
                    value += self.spaces[i + move]
            elif i == s**2 - 1:
                for move in [
                    -1,
                    -s - 1,
                    -s,
                    -2 * s + 1,
                    -s + 1,
                    -i,
                    -i + s - 1,
                    -i + s - 2,
                ]:
                    value += self.spaces[i + move]
            elif i % s == 0:
                for move in [-s, s, -1, s - 1, 2 * s - 1, -s + 1, s + 1, 1]:
                    value += self.spaces[i + move]
            elif i % s == s - 1:
                for move in [-s, s, -1, s - 1, -2 * s + 1, -s - 1, -s + 1, 1]:
                    value += self.spaces[i + move]
            elif i // s == 0:
                for move in [-s, s, -1, s - 1, s + 1, -s - 1, -s + 1, 1]:
                    value += self.spaces[i + move]
            elif i // s == s - 1:
                for move in [
                    -1,
                    -s - 1,
                    -s,
                    -s + 1,
                    1,
                    -i + i % s,
                    -i + i % s - 1,
                    -i + i % s + 1,
                ]:
                    value += self.spaces[i + move]
            if value == 3:
                iteration[i] = 1
            elif value == 2 and self.spaces[i]:
                iteration[i] = 1
            else:
                iteration[i] = 0
        self.spaces = iteration


def main():
    import pygame

    SIZE = 16
    HEIGHT = WIDTH = 640
    TILE = HEIGHT // SIZE
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FPS = 5

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode([HEIGHT, WIDTH])
    pygame.display.set_caption("Conway's Game Of Life")
    board = Board(SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.KEYUP:
        board.iterate()
        for i in range(SIZE**2):
            rect = (i % SIZE * TILE, (SIZE - i // SIZE - 1) * TILE, TILE, TILE)
            if board.spaces[i]:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
