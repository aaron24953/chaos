import random

starting_dice = [4, 6, 8, 10, 10, 12, 20]


def show_rolls():
    output = ""
    for die, roll in zip(dice, rolls):
        output += f"D{die}: {roll}  "
    print(output)


results = []
wins = 0
for i in range(100000):
    dice = [die for die in starting_dice]
    fails = 0
    removed_dice = []
    while dice and fails <= len(removed_dice):
        rolls = [random.randint(1, die) for die in dice]
        # show_rolls()
        success = False
        remove = []
        for die, roll in zip(dice, rolls):
            if die == roll:
                success = True
                removed_dice.append(die)
                remove.append(die)
        for die in remove:
            dice.remove(die)
        if success:
            fails = 0
        else:
            fails += 1
        # print(rolls, dice, success, removed_dice, fails)
    results.append(removed_dice)

removed_count = [len(result) for result in results]
counts = []
for i in range(len(starting_dice)+1):
    counts.append(removed_count.count(i)*100/len(removed_count))

for j in [f"{i}: {counts[i]}%" for i in range(len(counts))]:
    print(j)
