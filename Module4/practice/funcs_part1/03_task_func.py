# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: your code here
    pass

import math
def distance(x1, y1, x2, y2):
    c = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return c
print (distance(0, 0, 1, 0))
