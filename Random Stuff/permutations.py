from factorial import factorial as fact


def permute(array):
    print(array)
    leng = len(array)
    facts = [fact(leng - i) for i in range(leng + 1)]
    perms = []
    print(facts[0])
    for i in range(facts[0]):
        perm = []
        indexes = [j for j in range(leng)]
        for j in range(leng):
            index = (i // facts[j + 1]) % (leng - j)
            perm.append(array[indexes[index]])
            indexes.remove(indexes[index])
        perms.append(perm)
    return perms
