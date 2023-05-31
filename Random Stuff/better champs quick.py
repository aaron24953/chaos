file = open("message.txt", "r")
text = file.readlines()
names = []
for i in range(0, len(text), 2):
    names.append(text[i][1:-1])


numChamps = len(names)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if input((array[j], pivot)) == "l":  # adasdasd
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


quickSort(names, 0, numChamps - 1)
print(names)

file = open("results quick.txt", "w")
for name in names:
    file.write(f"{name}\n")
file.close()
