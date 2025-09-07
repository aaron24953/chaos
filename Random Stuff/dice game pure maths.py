from functools import cache

dice = (4, 6, 8, 10, 10, 12, 20)
# 4, 6, 8, 10, 10, 12, 20
initial_attempts = 1
starting_dice_count = len(dice)


@cache
def win_odds(dice, attempts_left, starting_dice_count):
    if not dice:
        return 1
    if attempts_left == 0:
        return 0
    elif len(dice) == 1:
        return 1-((dice[0]-1)/dice[0])**attempts_left

    win_chance = 0
    miss_chance = 1
    for die in dice:
        miss_chance *= (die-1)/die
    win_chance += miss_chance * win_odds(dice,
                                         attempts_left-1,
                                         starting_dice_count)
    for i in range(1, 2**len(dice)):
        results = bin(i).replace("b", "0"*len(dice))[::-1]
        next_dice = []
        chance = 1
        for j in range(len(dice)):
            if results[j] == "0":
                next_dice.append(dice[j])
                chance *= (dice[j]-1)/dice[j]
            else:
                chance /= dice[j]
        win_chance += chance * win_odds(tuple(next_dice),
                                        starting_dice_count - len(next_dice)+1,
                                        starting_dice_count)
    return win_chance


print(f"{win_odds(dice, initial_attempts, starting_dice_count)*100}%")
