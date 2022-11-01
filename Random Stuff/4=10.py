from typing import List, Union
from permutations import permute

SIZE = 4
TO_TEST = [8, 9, 2, 6]
RESTRICTIONS = []
TARGET = 10


def calc(toCalc: List[Union[int, float]]):  # [num,symbol,num...
    done: List[int] = []
    for i in range(1, len(toCalc) - 1, 2):
        if toCalc[i] == 3:
            if toCalc[i + 1] == 0:
                return 2**64 - 1
            toCalc[i + 1] = toCalc[i - 1] / toCalc[i + 1]
            done.append(i)
        elif toCalc[i] == 2:
            toCalc[i + 1] = toCalc[i - 1] * toCalc[i + 1]
            done.append(i)
    for i in range(len(done) - 1, -1, -1):
        toCalc.pop(done[i])
        toCalc.pop(done[i] - 1)
    done = []
    for i in range(1, len(toCalc) - 1, 2):
        if toCalc[i] == 1:
            toCalc[i + 1] = toCalc[i - 1] - toCalc[i + 1]
            done.append(i)
        elif toCalc[i] == 0:
            toCalc[i + 1] = toCalc[i - 1] + toCalc[i + 1]
            done.append(i)
    for i in range(len(done) - 1, -1, -1):
        toCalc.pop(done[i])
        toCalc.pop(done[i] - 1)
    return toCalc[0]


def test(number: List[int], restrictions: List[int] = []):
    possible: List[List[int]] = []
    numbers = permute(number)
    for number in numbers:
        for operator in operators:
            restricted = False
            for op in operator:
                if op in restrictions:
                    restricted = True
            if not restricted:
                toCalc: List[Union[int, float]] = [
                    (number[i // 2] if i % 2 == 0 else operator[i // 2])
                    for i in range(SIZE * 2 - 1)
                ]
                if calc(toCalc) == TARGET:
                    possible.append(
                        [
                            (number[i // 2] if i % 2 == 0 else operator[i // 2])
                            for i in range(SIZE * 2 - 1)
                        ]
                    )
    return possible


def make_nice(equation: List[int]):
    nice = ""
    symbols = ["+", "-", "*", "/"]
    for i in range(len(equation)):
        if i % 2 == 0:
            nice = f"{nice}{equation[i]}"
        else:
            nice = f"{nice}{symbols[equation[i]]}"
    return nice


numbers: List[List[int]] = []
for i in range(10**SIZE):
    number = [(i // 10 ** (SIZE - 1 - j)) % 10 for j in range(SIZE)]
    numbers.append(number)

operators: List[List[int]] = []
for i in range(4 ** (SIZE - 1)):
    operator = [(i // 4 ** (SIZE - 2 - j)) % 4 for j in range(SIZE - 1)]
    operators.append(operator)


def all_valid():
    valid: List[List[int]] = []
    for number in numbers:
        for operator in operators:
            toCalc: List[Union[int, float]] = [
                (number[i // 2] if i % 2 == 0 else operator[i // 2])
                for i in range(SIZE * 2 - 1)
            ]
            if calc(toCalc) == TARGET:
                valid.append(
                    [
                        (number[i // 2] if i % 2 == 0 else operator[i // 2])
                        for i in range(SIZE * 2 - 1)
                    ]
                )
                # print(make_nice(valid.pop()))  # remove
    return valid


if __name__ == "__main__":
    print([make_nice(eq) for eq in test(TO_TEST, RESTRICTIONS)])
    print(len([make_nice(equation) for equation in all_valid()]))
