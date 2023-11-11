from random import shuffle

deck = [i % 13 + 1 for i in range(52)]
scores: list[int] = []
numi = 1000000

for i in range(numi):
    failed = False
    score = 0
    while not failed:
        if deck[score] <= 7:
            guess = "h"
        else:
            guess = "l"
        answer = (
            "h"
            if deck[score + 1] > deck[score]
            else "l"
            if deck[score + 1] < deck[score]
            else "f"
        )
        if guess == answer:
            score += 1
        else:
            failed = True
    scores.append(score)
    shuffle(deck)


output = ""

chances = [scores.count(i) / numi for i in range(52)]

for i in range(52):
    output += f"{i}: {chances[i]}\n"

print(output, sum([chances[i] for i in range(12, 52)]))
