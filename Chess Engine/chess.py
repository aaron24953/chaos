import random
from typing import List, Tuple, Union
from singleton import Singleton
import pygame

GUI = True
WIDTH = 640
HEIGHT = 640
SIZE = 80
PLAYER = [True, False]  # true for human
PAIN = True

pygame.init()


class Board:
    def __init__(self):
        self.spaces: List[Union[Space,
                                Pawn,
                                Knight,
                                Bishop,
                                Rook,
                                Queen,
                                King,
                                ]] = [Space(i) for i in range(64)]
        self.turn: int = 0
        self.kingPositions: List[int] = [-1, -1]
        self.history: List[Tuple[int, int, Union[
            Space,
            Pawn,
            Knight,
            Bishop,
            Rook,
            Queen,
            King,
            ]]] = []

    def move(self, start: int, move: int) -> int:
        end = start + move
        if not move:
            return 0
        if end >= 64 or end < 0:
            return 0
        if self.spaces[start] == Space():
            print("thats a space")
            return 0
        if self.spaces[start].colour != self.turn % 2:
            return 0
        val: int = self.spaces[start].validate_move(start, move, self)
        if val:
            replaced = self.spaces[end]
            self.spaces[end] = self.spaces[start]
            self.spaces[start] = Space()
            if val == 2:
                self.spaces[end - 8] = Space()
            elif val == 3:
                self.spaces[end + 8] = Space()
            self.turn += 1
            self.history.append((start, end, replaced))
        return 1

    def load_FEN(self, fen: str) -> None:
        fenLines = fen.split("/")
        skiped = 0
        fenLetter = " "
        for i in range(64):
            do = True
            if i % 8 == 0:
                skip = 0
                skiped = 0
            try:
                fenLetter = fenLines[i // 8][i % 8]
            except BaseException:
                do = False
            if do:
                try:
                    num = int(fenLetter)
                except BaseException:
                    num = False
                if not num:
                    if fenLetter == " ":
                        colour = -1
                    elif fenLetter == fenLetter.upper():
                        colour = 1
                    else:
                        colour = 0
                    fenLetter = fenLetter.lower()
                    if fenLetter == "p":
                        self.spaces[i + skiped] = Pawn(colour, i // 8)
                    elif fenLetter == "r":
                        self.spaces[i] = Rook(colour)
                    elif fenLetter == "n":
                        self.spaces[i] = Knight(colour)
                    elif fenLetter == "b":
                        self.spaces[i] = Bishop(colour)
                    elif fenLetter == "q":
                        self.spaces[i] = Queen(colour)
                    elif fenLetter == "k":
                        self.spaces[i] = King(colour)
                        self.kingPositions[colour] = i
                else:
                    skip = num - 1
                    skiped += skip

    def text_display(self):
        list: List[str] = []
        colour = 0
        o = ""
        for i in range(64):
            if i % 8 == 0:
                o = ""
            try:
                letter = self.spaces[i].symbol
                colour = self.spaces[i].colour
            except BaseException:
                letter = " "
            if colour:
                letter = letter.upper()
            o += letter
            if i % 8 == 7:
                list.append(o)
            else:
                o += "|"
        for i in range(7, -1, -1):
            print(list[i])

    def startPos(self):
        self.load_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w")

    def checkForCheck(self) -> bool:
        kingPosition = self.kingPositions[self.turn % 2]
        kingColour = self.spaces[kingPosition].colour
        for possibleMove in [17, 15, 10, 6, -17, -15, -10, -6]:
            if isinstance(self.spaces[kingPosition + possibleMove], Knight):
                if self.spaces[kingPosition +
                               possibleMove].colour != kingColour:
                    if self.spaces[kingPosition -
                                   possibleMove].validate_move(kingPosition -
                                                               possibleMove,
                                                               possibleMove,
                                                               self,
                                                               ):
                        return True
        for i in range(1, 8):
            for possibleMove in [-9, -8, -
                                 7, -1, 1, 7, 8, 9]:  # horendously inneficient
                if 0 <= kingPosition + possibleMove * i < 64:
                    if not isinstance(
                            self.spaces[kingPosition
                                        + possibleMove * i], Space):
                        if self.spaces[kingPosition +
                                       possibleMove * i].colour != kingColour:
                            if self.spaces[kingPosition +
                                           possibleMove *
                                           i].validate_move(kingPosition +
                                                            possibleMove *
                                                            i, -
                                                            possibleMove *
                                                            i, self):
                                return True
        return False

    def undo(self):
        start, end, replaced = self.history.pop()
        self.spaces[start] = self.spaces[end]
        self.spaces[end] = replaced


class Space(Singleton):
    def __init__(self, *args: int):
        self.args = args
        self.symbol = " "
        self.colour = -1
        self.jumped = -1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        return -1


class Pawn:
    def __init__(self, colour: int, vPos: int):
        self.symbol = "p"
        self.colour = colour
        self.jumped: int = -1
        if (vPos == 1 and colour == 0) or (vPos == 6 and colour == 1):
            self.jump = True
        else:
            self.jump = False

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        if self.colour == 0:
            if isinstance(board.spaces[end], Space):
                if move == 8 or (self.jump and move == 16):
                    if move == 16:
                        if not isinstance(
                                board.spaces[end - 8], Space):
                            return 0
                    self.jumped = board.turn
                    self.jump = False
                    return 1
            if isinstance(board.spaces[end - 8], Pawn):
                if board.spaces[end - 8].jumped == board.turn - 1:
                    if ((move == 7 and start % 8 != 0) or (
                            move == 9 and start % 8 != 7)):
                        return 2
            if ((
                    (move == 7 and start % 8 != 0)
                    or (move == 9 and start % 8 != 7)
                )
                    and not isinstance(board.spaces[end], Space)):
                if board.spaces[end].colour != self.colour:
                    return 1
                else:
                    return 0
        else:
            if isinstance(board.spaces[end], Space):
                if move == -8 or (self.jump and move == -16):
                    if move == -16:
                        if not isinstance(
                                board.spaces[end + 8], Space):
                            return 0
                    self.jumped = board.turn
                    self.jump = False
                    return 1
            if isinstance(board.spaces[end + 8], Pawn):
                if board.spaces[end + 8].jumped == board.turn - 1:
                    if ((move == -
                            7 and start %
                            8 != 7) or (move == -
                                        9 and start %
                                        8 != 0)):
                        return 3
            if ((
                    (move == -7 and start % 8 != 7)
                    or (move == -9 and start % 8 != 0))
                    and not isinstance(board.spaces[end], Space)):
                if board.spaces[end].colour != self.colour:
                    return 1
                else:
                    return 0
        return 0

    def possible_moves(self, start: int, board: Board) -> List[int]:
        possibleMoves: List[int] = []
        if not self.colour:
            if isinstance(board.spaces[start + 8], Space):
                possibleMoves.append(8)
            if isinstance(board.spaces[start + 16], Space):
                if self.jump:
                    possibleMoves.append(16)
            for move in [7, 9]:
                if ((move == 7 and start % 8 != 0) or (
                        move == 9 and start % 8 != 7)):
                    if not isinstance(
                            board.spaces[start + move], Space):
                        if board.spaces[start + move].colour:
                            possibleMoves.append(move)
                    if isinstance(board.spaces[start + move], Space):
                        if not isinstance(
                                board.spaces[start + move - 8], Space
                        ):
                            if board.spaces[start + move -
                                            8].jumped == board.turn:
                                possibleMoves.append(move)
        else:
            if isinstance(board.spaces[start + 8], Space):
                possibleMoves.append(8)
            if isinstance(board.spaces[start + 16], Space):
                if self.jump:
                    possibleMoves.append(16)
            for move in [-7, -9]:
                if ((move == -
                     9 and start %
                     8 != 0) or (move == -
                                 7 and start %
                                 8 != 7)):
                    if not isinstance(
                            board.spaces[start + move], Space):
                        if not board.spaces[start + move].colour:
                            possibleMoves.append(move)
                    if isinstance(board.spaces[start + move], Space):
                        if not isinstance(
                                board.spaces[start + move + 8], Space
                        ):
                            if board.spaces[start + move +
                                            8].jumped == board.turn:
                                possibleMoves.append(move)
        return possibleMoves


class Knight:
    def __init__(self, colour: int):
        self.symbol = "n"
        self.colour = colour
        self.jumped = -1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        # 17,15,10,6
        end = start + move
        if not isinstance(board.spaces[end], Space):
            if board.spaces[end].colour == self.colour:
                return 0
        if abs(move) in [17, 15, 10, 6]:
            if 1 < start % 8 < 6:
                return 1
            elif move in [17, -15] and start % 8 < 7:
                return 1
            elif move in [-17, 15] and start % 8 > 0:
                return 1
        return 0

    def possible_moves(self, start: int, board: Board):  # bad
        possibleMoves: List[int] = []
        for i in [17, 15, 10, 6, -6, -10, -15, -17]:
            if self.validate_move(start, i, board):
                possibleMoves.append(i)
        return possibleMoves


class Bishop:
    def __init__(self, colour: int):
        self.symbol = "b"
        self.colour = colour
        self.jumped = -1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        print(start, move, end)
        if not isinstance(board.spaces[end], Space):
            if board.spaces[end].colour == self.colour:
                return 0
        moves = [-9, -7, 7, 9]
        if move in moves:
            return 1
        else:
            if move % 7 and move % 9:
                return 0
            if move % 7 == 0 and move > 0:
                if end % 8 > start % 8:
                    return 0
                for i in range(move // 7):
                    if board.spaces[start + 7 + i * 7] != Space():
                        return 0
            elif move % 9 == 0 and move > 0:
                if end % 8 < start % 8:
                    return 0
                for i in range(move // 9):
                    if board.spaces[start + 9 + i * 9] != Space():
                        return 0
            elif move % 9 == 0 and move < 0:
                if end % 8 > start % 8:
                    return 0
                for i in range(abs(move // 9)):
                    if board.spaces[start - 9 - i * 9] != Space():
                        return 0
            elif move % 7 == 0 and move < 0:
                if end % 8 < start % 8:
                    return 0
                for i in range(abs(move // 7)):
                    if board.spaces[start - 7 - i * 7] != Space():
                        return 0
            else:
                print("pain")
                return 0
        return 1

    def possible_moves(self, start: int, board: Board) -> List[int]:
        possibleMoves: List[int] = []
        for i in range(1, 8):
            for pMove in [-9, -7, 7, 9]:
                if Bishop.validate_move(self, start, i * pMove, board):
                    possibleMoves.append(i * pMove)
        return possibleMoves


class Rook:
    def __init__(self, colour: int):
        self.symbol = "r"
        self.castle = True
        self.colour = colour
        self.jumped = -1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        if not isinstance(board.spaces[end], Space):
            if board.spaces[end].colour == self.colour:
                return 0
        if move % 8 == 0:
            for i in range(1, abs(move // 8)):
                if move == abs(move):
                    if not isinstance(
                            board.spaces[start + 8 * i], Space):
                        return 0
                elif (
                    not isinstance(board.spaces[start - 8 * i], Space)
                ):
                    return 0
            return 1
        if move < 8:
            if move == abs(move):
                if move % 8 < end % 8:
                    for i in range(1, move):
                        if not isinstance(
                                board.spaces[start + i], Space):
                            return 0
                    return 1
            else:
                if move % 8 > end % 8:
                    for i in range(1, move):
                        if not isinstance(
                                board.spaces[start - i], Space):
                            return 0
                    return 1
        return 0

    def possible_moves(self, start: int, board: Board) -> List[int]:
        possibleMoves: List[int] = []
        for i in range(1, 8):
            for pMove in [-8, -1, 1, 8]:
                if Rook.validate_move(self, start, i * pMove, board):
                    possibleMoves.append(pMove * i)
        return possibleMoves


class Queen:
    def __init__(self, colour: int):
        self.colour = colour
        self.symbol = "q"
        self.castle = False
        self.jumped = -1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        return Rook.validate_move(
            self, start, move, board) or Bishop.validate_move(  # type: ignore
            self, start, move, board)  # type: ignore

    def possible_moves(self, start: int, board: Board) -> List[int]:
        return (
            Rook.possible_moves(self, start, board)  # type: ignore
            + Bishop.possible_moves(self, start, board)  # type: ignore
        )  # type: ignore


class King:
    def __init__(self, colour: int):
        self.colour = colour
        self.symbol = "k"
        self.castle = True
        self.jumped = -1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        if move not in [-9, -8, -7, -1, 1, 7, 8, 9]:
            return 0
        if move in [-9, -1, 7]:
            if end % 8 == start % 8 - 1:
                return 1
        elif move in [-7, 1, 9]:
            if end % 8 == start % 8 + 1:
                return 1
        else:
            return 1
        return 0


def text_input() -> tuple[int, int]:
    start: int = int(input("start?"))
    move: int = int(input("move?"))
    return start, move


def main() -> None:
    from chessAI import generate_AI_move
    gBoard = Board()
    # gBoard.startPos()
    gBoard.load_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w")
    running = True
    if GUI:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        pygame.display.set_caption("Chess")
        selected = -1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and PLAYER[gBoard.turn % 2]
                ):
                    mousePos = pygame.mouse.get_pos()
                    if selected == -1:
                        selected = (
                            mousePos[0] // SIZE + 56 - 8 * (
                                mousePos[1] // SIZE
                            )
                        )
                    elif PLAYER[gBoard.turn % 2]:
                        end = (
                            mousePos[0] // SIZE + 56 - 8 * (
                                mousePos[1] // SIZE
                            )
                        )
                        gBoard.move(selected, end-selected)
                        selected = -1
                    else:
                        AIMove = generate_AI_move(gBoard)
                        gBoard.move(AIMove[0], AIMove[1])
            for i in range(64):
                if i == selected:
                    pygame.draw.rect(
                        screen,
                        (0, 0, 255),
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                elif (i + i // 8) % 2:
                    pygame.draw.rect(
                        screen,
                        (255, 0, 255),
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (255, 0, 150),
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                if gBoard.spaces[i] != Space():
                    if not PAIN:
                        sprite = pygame.image.load(
                            'Chess Engine/'
                            f'{gBoard.spaces[i].symbol}'
                            f'{gBoard.spaces[i].colour}.png'
                        )
                    else:
                        sprite = pygame.image.load(
                            'Chess Engine/'
                            f'{random.choice(["k", "q", "n", "b", "r", "p"])}'
                            f'{random.randint(0,1)}.png'
                        )
                    screen.blit(sprite, (i % 8 * SIZE, (7 - i//8) * SIZE))

            pygame.display.flip()
    else:
        while running:
            gBoard.text_display()
            input_ = text_input()
            if input_[0] == -1:
                gBoard.undo()
            else:
                gBoard.move(input_[0], input_[1])


if __name__ == "__main__":
    main()

pygame.quit()
