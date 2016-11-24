from turtle import *
from numpy import exp


def movement(iterations=1, directs=None, length=None):
    if not directs:
        directs = [0]
    if not length:
        length = 1000 / exp(iterations)
    for i in directs:
        if i == 0:
            if iterations != 0:
                movement(iterations - 1, [0, 1, 0, 2, 0, 1, 0], length)
            else:
                forward(length)
        elif i == 1:
            left(60)
        elif i == 2:
            right(120)

iterations = 5
movement(iterations)