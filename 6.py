from turtle import *
from numpy import exp


def movement(iterations=1, directs=None, length=None):
    p = False
    if not directs:
        directs = [0]
    if not length:
        length = 1000 / 2 ** iterations
    for i in directs:
        if i == 0:
            if iterations != 0:
                if not p:
                    movement(iterations - 1, [1, 0, 2, 0, 1], length)
                    p = True
                else:
                    movement(iterations - 1, [4, 0, 3, 0, 4], length)
            else:
                forward(length)
        elif i == 1:
            left(45)
        elif i == 2:
            right(90)
        elif i == 3:
            left(90)
        elif i == 4:
            right(45)

iterations = 6
movement(iterations)
input()