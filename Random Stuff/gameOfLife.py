import random


class Board():
    def __init__(self, size: int):
        self.size = size
        self.spaces = [0 for i in range(size**2)]  # type: ignore

    def iterate(self):
        iteration = self.spaces
        for i in range(len(iteration)):
            value = 0
            value += self.spaces[i]
            iteration[i - 1] = value
            if random.random() < 0.2:
                iteration[i - 1] = 1
        self.spaces = iteration
        print(self.spaces)


def main():
    import pygame

    SIZE = 8
    HEIGHT = WIDTH = 640
    TILE = HEIGHT // SIZE
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FPS = 30

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
            elif event.type == pygame.KEYUP:
                board.iterate()
        for i in range(SIZE ** 2):
            if board.spaces[i]:
                pygame.draw.rect
                (
                    screen, WHITE,
                    (
                        i % SIZE * TILE,
                        (SIZE - i // SIZE - 1) * TILE, TILE, TILE
                    ))
            else:
                pygame.draw.rect
                (
                    screen, BLACK,
                    (
                        i % SIZE * TILE,
                        (SIZE - i // SIZE - 1) * TILE, TILE, TILE
                    ))
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
