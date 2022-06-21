import chess
import random


def generate_AI_move(board: chess.Board) -> tuple[int, int]:  # [start, move]
    allMoves = board.all_moves()
    picked = False
    i = 0
    while not picked and i < 1000:
        start = random.randint(0, 63)
        i += 1
        if i % 1000 == 0:
            print(i)
        if allMoves[start] and board.spaces[start].colour == board.turn % 2:
            picked = True
            print(start, allMoves[start])
            return (start, random.choice(allMoves[start]))
    return (-1, -1)


def main():
    board = chess.Board()
    board.startPos()
    print(generate_AI_move(board))


if __name__ == "__main__":
    main()
