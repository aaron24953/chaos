lst = [1, 6, 4, "f", "s"]
from itertools import combinations as c

for combo in c(lst, 2):  # 2 for pairs, 3 for triplets, etc
    print(combo[0])
    print(combo)
