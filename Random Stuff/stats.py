# stats between

files = []
files.append(open("correct.txt", "r").readlines())
files.append(open("natat.txt", "r").readlines())
files.append(open("not panda.txt", "r").readlines())
files.append(open("format.txt", "r").readlines())
files[-1] = [files[-1][i][1:] for i in range(0, len(files[-1]), 2)]
for i in range(len(files)):
    files[i] = [files[i][j][:-1] for j in range(len(files[i]))]

file = open("message.txt", "r")
text = file.readlines()
names = []
for i in range(0, len(text), 2):
    names.append(text[i][1:-1])

for i in range(len(files)):
    for j in range(len(files[i])):
        files[i][j] = names.index(files[i][j])

placements = []
for i in range(len(names)):
    placement = []
    for j in range(len(files)):
        placement.append(files[j].index(i))
    placements.append(placement)

differences = []
for placement in placements:
    difference = []
    for i in range(len(placement)):
        for j in range(i + 1, len(placement)):
            difference.append(abs(placement[i] - placement[j]))

    differences.append(
        (
            round(sum(difference) / ((len(files) ** 2 + len(files)) / 2), 2),
            names[placements.index(placement)],
        )
    )
differences.sort()
print(differences)

champPlaces = [
    (round(sum(placements[i]) / len(placements[i]) + 1, 2), names[i])
    for i in range(len(placements))
]

# champPlaces.sort()

# champPlaces = [champ[1] for champ in champPlaces]
# champPlaces = "\n".join(champPlaces)
# print(champPlaces)
