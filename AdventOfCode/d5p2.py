# d5p2

from d5data import stack, moves

stack = stack.split("\n")
stack = [stack [len(stack)-i-1] for i in range(len(stack))]
stack = [[stac[i] for stac in stack] for i in range(1, len(stack[0]), 4)]
for stac in stack:
    while " " in stac:
        stac.remove(" ")

moves = moves.split("\n")
moves = [move.split(" ") for move in moves]
moves = [(int(move[1]), int(move[3]), int(move[5])) for move in moves]


for move in moves:
    stac = []
    for i in range(move[0]):
        if stack[move[1]-1]:
            stac.append(stack[move[1]-1].pop())
    [stack[move[2]-1].append(stac.pop()) for i in range(len(stac))]

print("".join([stac.pop() for stac in stack]))
