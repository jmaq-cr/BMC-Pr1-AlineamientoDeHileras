from __future__ import division, print_function
from src.utilities import *

pt = {'match': 2, 'mismatch': -1, 'gap': -1}


def mch(alpha, beta):
    if alpha == beta:
        return pt['match']
    elif alpha == '-' or beta == '-':
        return pt['gap']
    else:
        return pt['mismatch']


def water(s1, s2):
    m, n = len(s1), len(s2)
    H = crearMatriz(m + 1, n + 1)
    T = crearMatriz(m + 1, n + 1)
    max_score = 0
    # Score, Pointer Matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sc_diag = getValue(H,i-1,j-1) + mch(s1[i - 1], s2[j - 1])
            sc_up = getValue(H,i,j-1) + pt['gap']
            sc_left = getValue(H,i-1,j) + pt['gap']
            H = setValue(H,i,j,max(0, sc_left, sc_up, sc_diag))
            if getValue(H,i,j) == 0:
                T = setValue(T,i,j,0)
            if getValue(H,i,j) == sc_left:
                T = setValue(T, i, j, 1)
            if getValue(H,i,j) == sc_up:
                T = setValue(T, i, j, 2)
            if getValue(H,i,j) == sc_diag:
                T = setValue(T, i, j, 3)
            if getValue(H,i,j) >= max_score:
                max_i = i
                max_j = j
                max_score = getValue(H,i,j)


    align1, align2 = '', ''
    i, j = max_i, max_j

    # Traceback
    while getValue(T,i,j) != 0:
        if getValue(T,i,j) == 3:
            a1 = s1[i - 1]
            a2 = s2[j - 1]
            H = addDirection(H, i, j, "diag")
            i -= 1
            j -= 1
        elif getValue(T,i,j) == 2:
            a1 = '-'
            a2 = s2[j - 1]
            H = addDirection(H, i, j, "left")
            j -= 1
        elif getValue(T,i,j) == 1:
            a1 = s1[i - 1]
            a2 = '-'
            H = addDirection(H,i,j,"up")
            i -= 1
        align1 += a1
        align2 += a2

    align1 = align1[::-1]
    align2 = align2[::-1]
    sym = ''
    iden = 0
    for i in range(len(align1)):
        a1 = align1[i]
        a2 = align2[i]
        if a1 == a2:
            sym += a1
            iden += 1
        elif a1 != a2 and a1 != '-' and a2 != '-':
            sym += ' '
        elif a1 == '-' or a2 == '-':
            sym += ' '


    showMatrix(H, s1, s2)
    identity = iden / len(align1) * 100
    print('Identity = %f percent' % identity)
    print('Score =', max_score)
    print(align1)
    print(sym)
    print(align2)

if __name__ == '__main__':
    water("ATTGTGATCC", "TTGCATCGGC")