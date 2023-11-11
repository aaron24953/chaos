text = open("items.txt")

lines = text.readlines()
lines = [lines[5 * i + 2][:-1] for i in range(len(lines) // 5)]
print(",".join(lines))
