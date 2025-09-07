# optimal setup finder for dilation tree

ANIMAL_POINTS = 40000
ETERNITIES = 10**8
DILATION_UPGRADE_2 = 1400
SUPERNOVAS = 116
DILATION_TREE_POINTS = 16

"""
0,1 = 0, 13
1,1 = 14.94, 14.94
1,2 = 16.95, 30.41
1,3 = 19.04, 46.42
1,4 = 21.19, 63.02
1,5 = 23.43, 80.23
2,2 = 35.14, 35.14
2,3 = 40.22, 54.69
2,4 = 45.70, 75.76
2,5 = 51.62, 98.56
3,3 = 63.93, 63.93
3,4 = 74.36, 90.67
3,5 = 86.20, 121
4,4 = 108, 108
4,5 = 130, 149
5,5 = 186, 186
"""

# bonuses[this,other]
bonuses = [
    [0, 0, 0, 0, 0, 0],
    [13, 14.94, 16.95, 19.04, 21.19, 23.43],
    [26, 30.41, 35.14, 40.22, 45.70, 51.62],
    [39, 46.42, 54.69, 63.93, 74.36, 86.20],
    [52, 63.02, 75.76, 90.67, 108.0, 130.0],
    [65, 80.23, 98.56, 121.0, 149.0, 186.0]
]
#              0      1     2       3        4            5       6
# levels = [centre, top2, top 4, middle 1, middle 4, bottom 3, bottom 4]


def calculate_total_mult(levels):
    mults = [1 for i in range(4)]

    if levels[0] > 0:
        mults[0] = (1+(1+levels[0])*0.0005)**ANIMAL_POINTS

    if levels[1] > 0:
        mults[1] = ETERNITIES**(1.75+(0.25*(levels[1])) * (1 +
                                bonuses[levels[6]][levels[2]]/100))

    if levels[3] > 0:
        mults[2] = ((1+0.077*(1+(levels[3]+1)*0.1*(1+bonuses[levels[4]]
                    [levels[4]]/100)))/1.077)**DILATION_UPGRADE_2

    if levels[5] > 0:
        mults[3] = ((1.75+0.25*(levels[5]))*(1+bonuses[levels[2]]
                    [levels[6]]/100))**SUPERNOVAS

    total_mult = 1/10**100
    for mult in mults:
        total_mult *= mult
    return total_mult


scores = []
loadouts = []
for i in range(6**7):
    levels = [i//(6**j) % 6 for j in range(7)]
    cost = sum(levels)
    if levels[1] > 0:
        cost += 1
    if levels[2] > 0:
        if levels[1] == 0:
            cost += 99
        cost += 1
    if levels[4] > 0:
        if levels[3] == 0:
            cost += 99
        cost += 2
    if levels[5] > 0:
        cost += 2
    if levels[6] > 0 and levels[5] == 0:
        cost += 99
    if levels[0] == 0:
        cost += 99

    if cost == DILATION_TREE_POINTS:
        scores.append(calculate_total_mult(levels))
        loadouts.append(levels)

print(max(scores))
optimal = loadouts[scores.index(max(scores))]
names = ["C1", "T2", "T4", "M1", "M4", "B3", "B4"]
for i in range(7):
    print(f"{names[i]}: {optimal[i]}")
