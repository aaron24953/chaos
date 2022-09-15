from OX import Board


def minmax(board: Board, depth: int) -> tuple[int, int]:
    if depth:
        if board.spaces == [0 * i for i in range(9)]:
            return (-1, 2)
        evals: list[tuple[int, int]] = []
        for i in range(9):
            turn = board.turn
            board.move(i)
            if turn != board.turn:
                evals.append((minmax(board, depth - 1)[0], i))
                board.undo()
        if evals:
            if board.turn % 2:
                for i in range(len(evals)):
                    if evals[i][0] == 2:
                        return evals[i]
            else:
                for i in range(len(evals)):
                    if evals[i][0] == 1:
                        return evals[i]
            for eval in evals:
                if eval[0] == 0:
                    return eval
            return evals[0]
        else:
            return (board.eval(), -1)
    return (board.eval(), -1)


def main():
    board = Board()
    print(minmax(board, 6))


if __name__ == "__main__":
    main()
