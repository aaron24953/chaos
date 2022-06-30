from chess import Board
import random


def generate_AI_move(board: Board) -> tuple[int, int]:  # [start, move]
    allMoves = board.all_moves(board.turn % 2)
    picked = False
    i = 0
    while not picked:
        start = random.randint(0, 63)
        i += 1
        if i % 1000 == 0:
            print(i)
        if allMoves[start] and board.spaces[start].colour == board.turn % 2:
            picked = True
            return (start, random.choice(allMoves[start]))
    return (-1, -1)


def eval(board: Board):
    if board.done:
        if board.turn % 2:
            return 100000
        else:
            return -100000
    val = 0
    for space in board.spaces:
        if space.colour == 1:
            val -= space.val
        elif space.colour == 0:
            val += space.val
    return val



def main():
    board = Board()
    board.startPos()
    print(generate_AI_move(board))


if __name__ == "__main__":
    main()
