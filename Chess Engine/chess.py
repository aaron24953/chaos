import random
from typing import List, Tuple, Union
from singleton import Singleton
import pygame

GUI = False
WIDTH = 640
HEIGHT = 640
SIZE = 80
PLAYER = [False, False]  # true for human
PAIN = False
FPS = 0

if PAIN:
    WHITE = (255, 0, 155)
    BLACK = (255, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
else:  # constants never redefined but still flagged
    WHITE = (255, 255, 255)  # type: ignore
    BLACK = (155, 155, 255)  # type: ignore
    RED = (255, 0, 0)  # type: ignore
    GREEN = (155, 255, 155)  # type: ignore
    BLUE = (0, 0, 155)  # type: ignore

pygame.init()
clock = pygame.time.Clock()


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
        self.done = False
        self.kingPositions: List[int] = [-1, -1]
        self.history: List[List[Tuple[
            Union[
                Space,
                Pawn,
                Knight,
                Bishop,
                Rook,
                Queen,
                King,
            ],
            int
        ]]] = []

    def move(self, start: int, move: int) -> int:
        end = start + move
        if not move:
            return 1
        if end >= 64 or end < 0:
            return 2
        if self.spaces[start] == Space():
            print("thats a space")
            return 3
        if self.spaces[start].colour != self.turn % 2:
            return 4
        val: int = self.spaces[start].validate_move(start, move, self)
        if val:
            changes: List[tuple[
                Union[
                    Space,
                    Pawn,
                    Knight,
                    Bishop,
                    Rook,
                    Queen,
                    King,
                ],
                int
                ]] = []
            changes.append((self.spaces[end], end))
            changes.append((self.spaces[start], start))
            self.spaces[end] = self.spaces[start]
            self.spaces[start] = Space()
            self.spaces[end].castle = False
            if self.spaces[end].symbol in ["k", "r"]:
                if self.spaces[end].moved == -1:  # type: ignore
                    self.spaces[end].moved = self.turn  # type: ignore
            if val == 2:
                changes.append((self.spaces[end - 8], end - 8))
                self.spaces[end - 8] = Space()
            elif val == 3:
                changes.append((self.spaces[end + 8], end + 8))
                self.spaces[end + 8] = Space()
            elif val == 4:
                self.spaces[end] = Queen(self.spaces[end].colour)
            elif val == 5:
                if end % 8 == 6:
                    changes.append((self.spaces[end - 1], end - 1))
                    changes.append((self.spaces[end + 1], end + 1))
                    self.spaces[end - 1] = self.spaces[end + 1]
                    self.spaces[end + 1] = Space()
                else:
                    changes.append((self.spaces[end - 2], end - 2))
                    changes.append((self.spaces[end + 1], end + 1))
                    self.spaces[end + 1] = self.spaces[end - 2]
                    self.spaces[end - 2] = Space()
            self.turn += 1
            self.history.append(changes)
            if self.check((self.turn - 1) % 2):
                self.undo()
                return 5
        else:
            return 6
        return 0

    def force_move(self, start: int, move: int):
        end = start + move
        val: int = self.spaces[start].validate_move(start, move, self)
        if val:
            changes: List[tuple[
                Union[
                    Space,
                    Pawn,
                    Knight,
                    Bishop,
                    Rook,
                    Queen,
                    King,
                ],
                int
                ]] = []
            changes.append((self.spaces[end], end))
            changes.append((self.spaces[start], start))
            self.spaces[end] = self.spaces[start]
            self.spaces[start] = Space()
            self.spaces[end].castle = False
            if self.spaces[end].symbol in ["k", "r"]:
                if self.spaces[end].moved == -1:  # type: ignore
                    self.spaces[end].moved = self.turn  # type: ignore
            if val == 2:
                changes.append((self.spaces[end - 8], end - 8))
                self.spaces[end - 8] = Space()
            elif val == 3:
                changes.append((self.spaces[end + 8], end + 8))
                self.spaces[end + 8] = Space()
            elif val == 4:
                self.spaces[end] = Queen(self.spaces[end].colour)
            elif val == 5:
                if end % 8 == 6:
                    changes.append((self.spaces[end - 1], end - 1))
                    changes.append((self.spaces[end + 1], end + 1))
                    self.spaces[end - 1] = self.spaces[end + 1]
                    self.spaces[end + 1] = Space()
                else:
                    changes.append((self.spaces[end - 2], end - 2))
                    changes.append((self.spaces[end + 1], end + 1))
                    self.spaces[end + 1] = self.spaces[end - 2]
                    self.spaces[end - 2] = Space()
            self.turn += 1
            self.history.append(changes)
            if self.check((self.turn - 1) % 2):
                self.undo()
                return 5
        else:
            return 6
        return 0

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

    def undo(self):
        if self.history:
            self.done = False
            changes = self.history.pop()
            self.turn -= 1
            for change in changes:
                self.spaces[change[1]] = change[0]
                piece = self.spaces[change[1]]
                pieceY = change[1] // 8
                if (
                    piece.symbol == "p"
                    and (
                        (pieceY == 1 and piece.colour == 0)
                        or (pieceY == 6 and piece.colour == 1)
                    )
                ):
                    piece.jump = True  # type: ignore
                    piece.jumped = -10
                if piece.symbol in ["r", "k"]:
                    if piece.moved == self.turn:  # type: ignore
                        piece.moved = -1  # type: ignore
                        piece.castle = True

    def all_moves(self, colour: int) -> List[List[int]]:
        allMoves: List[List[int]] = []
        allMoves = [
            (
                self.spaces[i].possible_moves(i, self)
                if self.spaces[i].colour == colour
                else []
            )
            for i in range(64)
        ]
        invalid: List[tuple[int, int]] = []
        for i in range(64):  # pretty bad
            for j in range(len(allMoves[i])):
                if self.move(i, allMoves[i][j]):
                    invalid.append((i, allMoves[i][j]))
                else:
                    self.undo()
        for no in invalid:
            allMoves[no[0]].remove(no[1])
        return allMoves

    def check(self, colour: int) -> bool:
        kingPos = -1
        check = False
        for i in range(64):
            if (
                self.spaces[i].symbol == "k"
                and self.spaces[i].colour == colour
            ):
                kingPos = i
        if kingPos == -1:
            print("no king?!?!?!?!")
            return True
        kingX = kingPos % 8
        for move in [17, 15, 10, 6, -6, -10, -15, -17]:
            if 0 <= kingPos + move < 64:
                if (
                    self.spaces[kingPos + move].symbol == "n"
                    and self.spaces[kingPos + move].colour != colour
                ):
                    check = True
        dirHit: List[bool] = [False, False, False, False]
        moves = [-8, -1, 1, 8]
        for i in range(4):
            for j in range(1, 8):
                move = j * moves[i]
                if 0 <= kingPos + move < 64:
                    if (
                        self.spaces[kingPos + move].symbol in ["q", "r"]
                        and self.spaces[kingPos + move].colour != colour
                        and (
                            i in [0, 3]
                            or (i == 1 and (kingPos + move) % 8 < kingX)
                            or (i == 2 and (kingPos + move) % 8 > kingX)
                        )
                        and not dirHit[i]
                    ):
                        check = True
                    if self.spaces[kingPos + move] != Space():
                        dirHit[i] = True
        dirHit: List[bool] = [False, False, False, False]
        moves = [-9, -7, 7, 9]
        for i in range(4):
            for j in range(1, 8):
                move = j * moves[i]
                if 0 <= kingPos + move < 64:
                    if (
                        self.spaces[kingPos + move].symbol in ["q", "b"]
                        and self.spaces[kingPos + move].colour != colour
                        and (
                            (i in [0, 2] and (kingPos + move) % 8 < kingX)
                            or (i in [1, 3] and (kingPos + move) % 8 > kingX)
                        )
                        and not dirHit[i]
                    ):
                        check = True
                    if self.spaces[kingPos + move] != Space():
                        dirHit[i] = True
        for move in [-9, -8, -7, -1, 1, 7, 8, 9]:
            if 0 <= kingPos + move < 64:
                if (
                    self.spaces[kingPos + move].colour != colour
                    and self.spaces[kingPos + move].symbol == "k"
                ):
                    check = True
        if colour:
            if (
                (
                    self.spaces[kingPos - 7].colour == 0
                    and self.spaces[kingPos - 7].symbol == "p"
                    and kingPos % 8 != 7
                )
                or (
                    self.spaces[kingPos - 9].colour == 0
                    and self.spaces[kingPos - 9].symbol == "p"
                    and kingPos % 8 != 0
                )
            ):
                check = True
        else:
            if (
                (
                    self.spaces[kingPos + 7].colour == 1
                    and self.spaces[kingPos + 7].symbol == "p"
                    and kingPos % 8 != 0
                )
                or (
                    self.spaces[kingPos + 9].colour == 1
                    and self.spaces[kingPos + 9].symbol == "p"
                    and kingPos % 8 != 7
                )
            ):
                check = True
        return check

    def checkMate(self) -> bool:
        allMoves = self.all_moves(self.turn % 2)
        for moves in allMoves:
            if moves:
                return False
        return True


class Space(Singleton):
    def __init__(self, *args: int):
        self.args = args
        self.symbol = " "
        self.colour = -1
        self.jumped = -10
        self.castle = False
        self.val = 0

    def validate_move(self, start: int, move: int, board: Board) -> int:
        return -1

    def possible_moves(self, start: int, board: Board) -> List[int]:
        return []


class Pawn:
    def __init__(self, colour: int, vPos: int):
        self.symbol = "p"
        self.colour = colour
        self.jumped: int = -10
        self.castle = False
        if (vPos == 1 and colour == 0) or (vPos == 6 and colour == 1):
            self.jump = True
        else:
            self.jump = False
        self.val = 1

    def validate_move(self, start: int, move: int, board: Board) -> int:
        # 4 = promote
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
                    if end//8 == 7:
                        return 4
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
                    if end//8 == 7:
                        return 4
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
                    if end//8 == 0:
                        return 4
                    return 1

            if ((move == -
                    7 and start %
                    8 != 7) or (move == -
                                9 and start %
                                8 != 0)):
                if isinstance(board.spaces[end + 8], Pawn):
                    if board.spaces[end + 8].jumped == board.turn - 1:
                        return 3
            if ((
                    (move == -7 and start % 8 != 7)
                    or (move == -9 and start % 8 != 0))
                    and not isinstance(board.spaces[end], Space)):
                if board.spaces[end].colour != self.colour:
                    if end//8 == 0:
                        return 4
                    return 1
                else:
                    return 0
        return 0

    def possible_moves(self, start: int, board: Board) -> List[int]:
        possibleMoves: List[int] = []
        if not self.colour:
            if isinstance(board.spaces[start + 8], Space):
                possibleMoves.append(8)
                if self.jump:
                    if isinstance(board.spaces[start + 16], Space):
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
                                            8].jumped == board.turn - 1:
                                possibleMoves.append(move)
        else:
            if isinstance(board.spaces[start - 8], Space):
                possibleMoves.append(-8)
                if self.jump:
                    if isinstance(board.spaces[start - 16], Space):
                        possibleMoves.append(-16)
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
                                            8].jumped == board.turn - 1:
                                possibleMoves.append(move)
        return possibleMoves


class Knight:
    def __init__(self, colour: int):
        self.symbol = "n"
        self.colour = colour
        self.jumped = -10
        self.castle = False
        self.val = 3

    def validate_move(self, start: int, move: int, board: Board) -> int:
        # 17,15,10,6
        end = start + move
        if not 0 <= end < 64:
            return 0
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
            elif move in [10, -6] and start % 8 < 6:
                return 1
            elif move in [6, -10] and start % 8 > 1:
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
        self.jumped = -10
        self.castle = False
        self.val = 3

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        if not 0 <= end < 64:
            return 0
        if not isinstance(board.spaces[end], Space):
            if board.spaces[end].colour == self.colour:
                return 0
        if move % 7 and move % 9:
            return 0
        if move % 7 == 0 and move > 0:
            if end % 8 > start % 8:
                return 0
            for i in range(1, move // 7):
                if board.spaces[start + i * 7] != Space():
                    return 0
        elif move % 9 == 0 and move > 0:
            if end % 8 < start % 8:
                return 0
            for i in range(1, move // 9):
                if board.spaces[start + i * 9] != Space():
                    return 0
        elif move % 9 == 0 and move < 0:
            if end % 8 > start % 8:
                return 0
            for i in range(1, abs(move // 9)):
                if board.spaces[start - i * 9] != Space():
                    return 0
        elif move % 7 == 0 and move < 0:
            if end % 8 < start % 8:
                return 0
            for i in range(1, abs(move // 7)):
                if board.spaces[start - i * 7] != Space():
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
        self.jumped = -10
        self.moved = -1
        self.val = 5

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        if not 0 <= end < 64:
            return 0
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
        if -8 < move < 8:
            if move == abs(move):
                if start % 8 < end % 8:
                    for i in range(1, move):
                        if not isinstance(
                                board.spaces[start + i], Space):
                            return 0
                    return 1
            else:
                if start % 8 > end % 8:
                    for i in range(1, abs(move)):
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
        self.jumped = -10
        self.val = 9

    def validate_move(self, start: int, move: int, board: Board) -> int:
        return Rook.validate_move(
            self, start, move, board) or Bishop.validate_move(  # type: ignore
            self, start, move, board)  # type: ignore

    def possible_moves(self, start: int, board: Board) -> List[int]:
        return (
            Rook.possible_moves(self, start, board)  # type: ignore
            + Bishop.possible_moves(self, start, board)  # type: ignore
        )


class King:
    def __init__(self, colour: int):
        self.colour = colour
        self.symbol = "k"
        self.castle = True
        self.jumped = -10
        self.moved = -1
        self.val = 999999999

    def validate_move(self, start: int, move: int, board: Board) -> int:
        end = start + move
        if not 0 <= end < 64:
            return 0
        if move not in [-9, -8, -7, -2, -1, 1, 2, 7, 8, 9]:
            return 0
        if self.colour == board.spaces[end].colour:
            return 0
        if move in [-9, -1, 7]:
            if end % 8 == start % 8 - 1:
                return 1
        elif move in [-7, 1, 9]:
            if end % 8 == start % 8 + 1:
                return 1
        elif move in [-8, 8]:
            return 1
        else:
            if (
                move == 2
                and isinstance(board.spaces[end - 1], Space)
                and isinstance(board.spaces[end], Space)
                and self.castle
                and board.spaces[end + 1].castle
            ):
                return 5
            if (
                move == -2
                and isinstance(board.spaces[end + 1], Space)
                and isinstance(board.spaces[end], Space)
                and isinstance(board.spaces[end - 1], Space)
                and self.castle
                and board.spaces[end - 2].castle
            ):
                return 5
        return 0

    def possible_moves(self, start: int, board: Board) -> List[int]:
        moves: List[int] = []
        for move in [-9, -8, -7, -2, -1, 1, 2, 7, 8, 9]:
            if self.validate_move(start, move, board):
                moves.append(move)
        return moves


def text_input() -> tuple[int, int]:
    start: int = int(input("start?"))
    move: int = int(input("move?"))
    return start, move


def main() -> None:
    from chessAI import generate_AI_move, eval
    pygame.font.init()
    FONT = pygame.font.SysFont('Comic Sans MS', 30)
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
                ):
                    if PLAYER[gBoard.turn % 2]:
                        mousePos = pygame.mouse.get_pos()
                        if selected == -1:
                            selected = (
                                mousePos[0] // SIZE + 56 - 8 * (
                                    mousePos[1] // SIZE
                                )
                            )
                        else:
                            end = (
                                mousePos[0] // SIZE + 56 - 8 * (
                                    mousePos[1] // SIZE
                                )
                            )
                            gBoard.move(selected, end-selected)
                            if gBoard.checkMate():
                                gBoard.done = True
                            selected = -1
                elif event.type == pygame.KEYUP:
                    gBoard.undo()
            if not PLAYER[gBoard.turn % 2]:
                AIMove = generate_AI_move(gBoard)
                if AIMove == (-1, -1):
                    gBoard.done = True
                else:
                    gBoard.move(AIMove[0], AIMove[1])
                    if gBoard.checkMate():
                        gBoard.done = True
            selectedMoves: List[int] = []
            if selected != -1:
                selectedMoves = (
                    gBoard.all_moves(gBoard.turn % 2)[selected]
                )
                selectedMoves = (
                    [
                        selectedMoves[j]
                        + selected for j in range(len(selectedMoves))]
                )
            kingPos = -1
            for i in range(64):
                if (i + i // 8) % 2:
                    pygame.draw.rect(
                        screen,
                        WHITE,
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        BLACK,
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                if (
                    gBoard.spaces[i].colour == gBoard.turn % 2
                    and gBoard.spaces[i].symbol == "k"
                ):
                    kingPos = i
                if i == selected:
                    pygame.draw.rect(
                        screen,
                        BLUE,
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                elif (i in selectedMoves):
                    pygame.draw.rect(
                        screen,
                        GREEN,
                        (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                    )
                elif i == kingPos:
                    if gBoard.check(gBoard.turn % 2):
                        pygame.draw.rect(
                            screen,
                            RED,
                            (i % 8 * SIZE, (7 - i//8) * SIZE, SIZE, SIZE)
                        )
                elif gBoard.done:
                    pygame.draw.rect(
                            screen,
                            RED,
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
            screen.blit(
                FONT.render(
                    f"eval: {eval(gBoard)}",
                    True, RED
                ),
                (0, 0)
            )
            pygame.display.flip()
            clock.tick(FPS)
    else:
        while running:
            gBoard.text_display()
            if PLAYER[gBoard.turn % 2]:
                input_ = text_input()
                if input_[0] == -1:
                    gBoard.undo()
                else:
                    gBoard.move(input_[0], input_[1])
            else:
                move = generate_AI_move(gBoard)
                gBoard.move(move[0], move[1])


if __name__ == "__main__":
    main()

pygame.quit()
