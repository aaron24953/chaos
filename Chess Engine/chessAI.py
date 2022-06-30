from typing import List
from chess import Board
import random
import time

mode = "minmax"
depth = 1  # 0 = own move only, 1 = own + reply, 2 = o+r+o, ect


def generate_AI_move(board: Board) -> tuple[int, int]:  # [start, move]
    if mode == "random":
        allMoves = board.all_moves(board.turn % 2)
        picked = False
        i = 0
        while not picked:
            start = random.randint(0, 63)
            i += 1
            if i % 1000 == 0:
                print(i)
            if (
                allMoves[start]
                and board.spaces[start].colour == board.turn % 2
            ):
                picked = True
                return (start, random.choice(allMoves[start]))
    elif mode == "minmax":
        startT = time.time()
        best = minmax(board, depth)
        endT = time.time()
        print(endT - startT, best)
        return (best[0], best[1])
    return (-1, -1)


def minmax(board: Board, depth: int) -> tuple[int, int, int]:  # start end eval
    evals: List[int] = []
    moves: List[tuple[int, int]] = []
    allMoves = board.all_moves(board.turn % 2)
    for i in range(64):
        for move in allMoves[i]:
            if not board.force_move(i, move):
                if depth:
                    moveVal = minmax(board, depth - 1)
                else:
                    moveVal = (i, move, eval(board))
                evals.append(moveVal[2])
                moves.append((i, move))
                board.undo()
    if not moves:
        return (-1, -1, 0)
    if board.turn % 2:
        move = moves[evals.index(min(evals))]
        return (move[0], move[1], min(evals))
    else:
        move = moves[evals.index(max(evals))]
        return (move[0], move[1], max(evals))


def eval(board: Board):
    if board.checkMate():
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
