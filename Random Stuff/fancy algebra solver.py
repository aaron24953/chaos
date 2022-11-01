# show is a bool for if it will print or return
from math import *


def quadSolv(a, b, c):
    root = b**2 - 4 * a * c
    num = -b
    return (
        (num + root ** (1 / 2)) / (2 * a),
        (num - root ** (1 / 2)) / (2 * a),
        str(num / (2 * a)) + "+/-(root" + str(root) + "/" + str(2 * a) + ")",
    )


def bracTwoo(a, b, c):
    print("WIP")


def threBrac(a, b, c, d, e, f):  # (ax+b)(cx+d)(ex+f)
    pThree = a * c * e
    pTwo = a * c * f + a * d * e + b * c * e
    pOne = a * d * f + b * d * e + b * c * f
    pZero = b * d * f
    print(pThree, "x^3", pTwo, "x^2", pOne, "x", pZero)


def simpSurd(a, b, show):  # arootb
    change = True
    squares = getSquar(int(b ** (1 / 2)))
    while change == True:
        change = False
        for x in range(len(squares)):
            if b % squares[x] == 0:
                b = b / squares[x]
                a = a * squares[x] ** (1 / 2)
                change = True
    if show:
        print(a, "root", b)
    else:
        return (a, b)


def ratiDeno(a, b, c, d, show):  # arootb/crootd
    c, d = simpSurd(c, d, False)
    c = c * d
    b = b * d
    a, b = simpSurd(a, b, False)
    if show:
        print(a, "root", b, "/", c)
    else:
        return (a, b, c)


def simpFrac():
    print("WIP")


def compSqar(a, b, c):
    if b > 0 and c - (b / 2) ** 2 < 0:
        print("(x+" + str(int(b / 2)) + ")^2" + str(int(c - (b / 2) ** 2)))
    elif b < 0 and c - (b / 2) ** 2 < 0:
        print("(x" + str(int(b / 2)) + ")^2" + str(int(c - (b / 2) ** 2)))
    elif b > 0:
        print("(x+" + str(int(b / 2)) + ")^2+" + str(int(c - (b / 2) ** 2)))
    else:
        print("(x" + str(int(b / 2)) + ")^2+" + str(int(c - (b / 2) ** 2)))


def getSquar(a):
    sNums = []
    for x in range(a):
        sNums.append((x + 2) ** 2)
    return sNums
