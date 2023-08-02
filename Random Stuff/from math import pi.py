from math import pi

r = 1
c = pi * r * 2
d = 100
area = [(r / d) * ((i + 1 / 2) * (c / d)) for i in range(0, d)]
print(area, sum(area), r**2 * pi)
