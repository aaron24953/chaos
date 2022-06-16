import chess


def generate_AI_move(board: chess.Board):
    return (8, 8)


def main():
    board = chess.Board()
    board.startPos()
    print(generate_AI_move(board))


if __name__ == "__main__":
    main()
