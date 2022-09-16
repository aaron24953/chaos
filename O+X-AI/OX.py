import sys
import pygame

pygame.init()


class Board:
    def __init__(self) -> None:
        self.spaces = [0 * i for i in range(9)]
        self.turn = 0
        self.moves: list[int] = []

    def eval(self):
        for i in range(3):
            if (
                self.spaces[i] == self.spaces[i + 3] == self.spaces[i + 6]
                and self.spaces[i] != 0
            ):
                return self.spaces[i]
            elif (
                self.spaces[i * 3] == self.spaces[i * 3 + 1] == self.spaces[i * 3 + 2]
                and self.spaces[i * 3] != 0
            ):
                return self.spaces[i * 3]

        if self.spaces[0] == self.spaces[4] == self.spaces[8]:
            return self.spaces[0]
        elif self.spaces[2] == self.spaces[4] == self.spaces[6]:
            return self.spaces[2]

        return 0

    def move(self, square: int):
        if not self.spaces[square] and not self.eval():
            self.spaces[square] = self.turn % 2 + 1
            self.turn += 1
            self.moves.append(square)

    def undo(self):
        if self.moves:
            move = self.moves.pop()
            self.spaces[move] = 0
            self.turn -= 1


def main():
    from AI import minmax  # type: ignore

    running = True
    xy = 450
    w = 5
    DEPTH = 7
    SIZE = (xy, xy)
    screen = pygame.display.set_mode(SIZE)
    board = Board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                square = mouse[1] // (xy // 3) * 3 + mouse[0] // (xy // 3)
                board.move(square)
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    board.undo()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    board.move(minmax(board, DEPTH)[1])

        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (xy / 3, 0), (xy / 3, xy), w)
        pygame.draw.line(screen, (255, 255, 255), (2 * xy / 3, 0), (2 * xy / 3, xy), w)
        pygame.draw.line(screen, (255, 255, 255), (0, xy / 3), (xy, xy / 3), w)
        pygame.draw.line(screen, (255, 255, 255), (0, 2 * xy / 3), (xy, 2 * xy / 3), w)

        for i in range(9):
            x = i % 3 * xy / 3
            y = i // 3 * xy / 3
            if board.spaces[i] == 1:
                pygame.draw.line(
                    screen, (255, 0, 255), (x, y), (x + xy / 3, y + xy / 3), w
                )
                pygame.draw.line(
                    screen, (255, 0, 255), (x + xy / 3, y), (x, y + xy / 3), w
                )
            elif board.spaces[i] == 2:
                pygame.draw.circle(
                    screen, (255, 0, 255), (x + xy / 6, y + xy / 6), xy / 6, w
                )
        eval = board.eval()
        if eval == 1:
            pygame.draw.line(screen, (255, 0, 255), (0, 0), (xy, xy), w * 3)
            pygame.draw.line(screen, (255, 0, 255), (xy, 0), (0, xy), w * 3)
        elif eval == 2:
            pygame.draw.circle(screen, (255, 0, 255), (xy / 2, xy / 2), xy / 2, w * 3)

        pygame.display.flip()


if __name__ == "__main__":
    main()
