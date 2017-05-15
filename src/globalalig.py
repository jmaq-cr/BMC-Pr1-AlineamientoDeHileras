from __future__ import print_function, division
from src.utilities import *

def mch(alpha, beta):
    if alpha == beta:
        return pt['match']
    elif alpha == '-' or beta == '-':
        return pt['gap']
    else:
        return pt['mismatch']


def needle(s2, s1):
    m, n = len(s1), len(s2)
    matriz = crearMatriz(m+1,n+1)

    # Initialization
    for i in range(m + 1): #puede que haya que quitar el + 1
        matriz = setValue(matriz, i, 0, pt['gap'] * i)
    for j in range(n + 1):
        matriz = setValue(matriz, 0, j, pt['gap'] * j)

    # Fill
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = getValue(matriz, i - 1, j - 1) + mch(s1[i - 1], s2[j - 1])
            delete = getValue(matriz, i - 1, j) + pt['gap']
            insert = getValue(matriz, i, j - 1) + pt['gap']
            matriz = setValue(matriz,i,j,max(diag, delete, insert))


    align1, align2 = '', ''
    i, j = m, n

    # Traceback
    while i > 0 and j > 0:
        score_current = getValue(matriz, i, j)
        score_diag = getValue(matriz, i-1, j-1)
        score_left = getValue(matriz, i, j-1)
        score_up = getValue(matriz, i-1, j)


        if score_current == score_diag + mch(s1[i - 1], s2[j - 1]):
            matriz = addDirection(matriz,i,j,"diag")
            a1, a2 = s1[i - 1], s2[j - 1]
            i, j = i - 1, j - 1
        if score_current == score_up + pt['gap']:
            matriz = addDirection(matriz,i,j,"up")
            a1, a2 = s1[i - 1], '-'
            i -= 1
        if score_current == score_left + pt['gap']:
            matriz = addDirection(matriz, i, j, "left")
            a1, a2 = '-', s2[j - 1]
            j -= 1

        align1 += a1
        align2 += a2

    while i > 0:
        a1, a2 = s1[i - 1], '-'
        align1 += a1
        align2 += a2
        i -= 1

    while j > 0:
        a1, a2 = '-', s2[j - 1]
        align1 += a1
        align2 += a2
        j -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]
    seqN = len(align1)
    sym = ''
    seq_score = 0
    ident = 0
    for i in range(seqN):
        a1 = align1[i]
        a2 = align2[i]
        if a1 == a2:
            sym += a1
            ident += 1
            seq_score += mch(a1, a2)

        else:
            seq_score += mch(a1, a2)
            sym += ' '

    ident = ident / seqN * 100

    if tablas:
        showMatrix(matriz, s1, s2)
    print('Identity = %2.1f percent' % ident)
    print('Score = %d\n' % seq_score)
    print(align1)
    print(sym)
    print(align2)

