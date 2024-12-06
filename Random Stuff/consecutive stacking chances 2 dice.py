# consecutive stacking chances

from random import randint
from math import floor, sqrt

runs: list[int] = []
NUM_RUNS = 1 * 10**8


victory = False
max_successes = 0
percent_complete = -1
for i in range(NUM_RUNS):
    last_percent_complete = percent_complete
    percent_complete = (i + 1) // (NUM_RUNS // 100)
    if percent_complete > last_percent_complete:
        print(percent_complete, "%")

    hasnt_failed = True
    successes = 0
    while hasnt_failed:
        roll = randint(1, 6) + randint(1, 6)
        should_be = floor(1 / 2 * (sqrt(8 * (successes + 0.5) + 9) - 1) + 1)
        if roll == should_be:
            successes += 1
        else:
            runs.append(successes)
            hasnt_failed = False

print(f"in {NUM_RUNS} runs, scores were:")
for i in range(max(runs) + 1):
    count = runs.count(i)
    print(f"{i}: {count}, {count/NUM_RUNS*100}%")
