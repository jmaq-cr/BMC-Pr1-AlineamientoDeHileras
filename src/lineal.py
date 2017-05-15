from __future__ import print_function, division
from src.utilities import *


def mch(alpha, beta):
    if alpha == beta:
        return pt['match']
    elif alpha == '-' or beta == '-':
        return pt['gap']
    else:
        return pt['mismatch']


def lineal(s1,s2):
    if len(s1) < len(s2):
        for i in range(len(s2)-len(s1)):
            s1 += "-"
    elif len(s1) > len(s2):
        for i in range(len(s1)-len(s2)):
            s2 += "-"

    result = []
    for i in range(len(s1)):
        result.append(mch(s1[i], s2[i]))

    score = sum(result)

    print("Seq 1:", s1)
    print("Seq 2:", s2)
    print("Score:", score)
