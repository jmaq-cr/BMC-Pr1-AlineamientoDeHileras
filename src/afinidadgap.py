from __future__ import print_function, division
from src.utilities import *

def mch(alpha, beta):
    if alpha == beta:
        return pt['match']
    elif alpha == '-' or beta == '-':
        return pt['gap']
    else:
        return pt['mismatch']


def afingap(s2, s1):
    m, n = len(s1), len(s2)
    A = crearMatriz(m+1,n+1)
    B = crearMatriz(m + 1, n + 1)
    C = crearMatriz(m + 1, n + 1)

    # Initialization
    for i in range(1, m + 1):
        A = setValue(A, i, 0, -1 * pt['opengap'] - (i - 1) * pt['extgap'])
        B = setValue(B, i, 0, -1 * pt['opengap'] - (i - 1) * pt['extgap'])

    for j in range(1, n + 1):
        A = setValue(A, 0, j, -1 * pt['opengap'] - (j - 1) * pt['extgap'])
        B = setValue(B, 0, j, -1 * pt['opengap'] - (j - 1) * pt['extgap'])


    # Fill A
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = getValue(A, i - 1, j - 1) + mch(s1[i - 1], s2[j - 1])
            delete = getValue(A, i - 1, j) + pt['gap']
            insert = getValue(A, i, j - 1) + pt['gap']
            A = setValue(A,i,j,max(diag, delete, insert))

    # Fill B
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            value = max(getValue(B, i - 1, j)-pt['opengap'],getValue(B, i - 1, j)-pt['extgap'])
            B = setValue(B, i, j, value)

    # Fill C
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            value = max(getValue(C, i, j - 1) - pt['opengap'], getValue(C, i, j - 1) - pt['extgap'])
            C = setValue(C, i, j, value)


    alignA1, alignA2 = '', ''
    i, j = m, n
    ident = 1

    # Traceback A
    while i > 0 and j > 0:
        score_current = getValue(A, i, j)
        score_diag = getValue(A, i-1, j-1)
        score_left = getValue(A, i, j-1)
        score_up = getValue(A, i-1, j)


        if score_current == score_diag + mch(s1[i - 1], s2[j - 1]):
            A = addDirection(A,i,j,"diag")
            a1, a2 = s1[i - 1], s2[j - 1]
            i, j = i - 1, j - 1
        if score_current == score_up + pt['gap']:
            A = addDirection(A,i,j,"up")
            a1, a2 = s1[i - 1], '-'
            i -= 1
        if score_current == score_left + pt['gap']:
            A = addDirection(A, i, j, "left")
            a1, a2 = '-', s2[j - 1]
            j -= 1

        alignA1 += a1
        alignA2 += a2

    while i > 0:
        a1, a2 = s1[i - 1], '-'
        alignA1 += a1
        alignA2 += a2
        i -= 1

    while j > 0:
        a1, a2 = '-', s2[j - 1]
        alignA1 += a1
        alignA2 += a2
        j -= 1

    alignA1 = alignA1[::-1]
    alignA2 = alignA2[::-1]
    seqNA = len(alignA1)
    symA = ''
    seq_scoreA = 0
    identA = 0
    for i in range(seqNA):
        a1 = alignA1[i]
        a2 = alignA2[i]
        if a1 == a2:
            symA += a1
            identA += 1
            seq_scoreA += mch(a1, a2)

        else:
            seq_scoreA += mch(a1, a2)
            symA += ' '

    alignB1, alignB2 = '', ''
    i, j = m, n

    # Traceback B
    while i > 0:
        score_current = getValue(B, i, j)
        score_diag = getValue(B, i - 1, j - 1)
        score_left = getValue(B, i, j - 1)
        score_up = getValue(B, i - 1, j)


        B = addDirection(B, i, j, "up")
        a1, a2 = s1[i - 1], '-'
        i -= 1


        alignB1 += a1
        alignB2 += a2



    while i > 0:
        a1, a2 = s1[i - 1], '-'
        alignB1 += a1
        alignB2 += a2
        i -= 1


    alignB1 = alignB1[::-1]
    alignB2 = alignB2[::-1]
    seqNB = len(alignB1)
    symB = ''
    seq_scoreB = 0
    identB = 0
    for i in range(seqNB):
        a1 = alignB1[i]
        a2 = alignB2[i]
        if a1 == a2:
            symB += a1
            identB += 1
            seq_scoreB += mch(a1, a2)

        else:
            seq_scoreB += mch(a1, a2)
            symB += ' '


    alignC1, alignC2 = '', ''
    i, j = m, n

    # Traceback C
    while j > 0:
        score_current = getValue(C, i, j)
        score_diag = getValue(C, i - 1, j - 1)
        score_left = getValue(C, i, j - 1)
        score_up = getValue(C, i - 1, j)

        C = addDirection(C, i, j, "left")
        a1, a2 = '-', s2[j - 1]
        j -= 1

        alignC1 += a1
        alignC2 += a2

    while j > 0:
        a1, a2 = '-', s2[j - 1]
        alignC1 += a1
        alignC2 += a2
        j -= 1

    alignC1 = alignC1[::-1]
    alignC2 = alignC2[::-1]
    seqNC = len(alignC1)
    symC = ''
    seq_scoreC = 0
    identC = 0
    for i in range(seqNC):
        a1 = alignC1[i]
        a2 = alignC2[i]
        if a1 == a2:
            symC += a1
            identC += 1
            seq_scoreC += mch(a1, a2)

        else:
            seq_scoreC += mch(a1, a2)
            symC += ' '

    if max(seq_scoreA,seq_scoreB,seq_scoreC) == seq_scoreA:
        print("A =")
        matriz = A
        seq_score = seq_scoreA
        align1 = alignA1
        align2 = alignA2
        sym = symA
        ident = identA / seqNA * 100
    elif max(seq_scoreA,seq_scoreB,seq_scoreC) == seq_scoreB:
        print("B =")
        matriz = B
        seq_score = seq_scoreB
        align1 = alignB1
        align2 = alignB2
        sym = symB
        ident = identB / seqNB * 100
    elif max(seq_scoreA,seq_scoreB,seq_scoreC) == seq_scoreC:
        print("C =")
        matriz = C
        seq_score = seq_scoreC
        align1 = alignC1
        align2 = alignC2
        sym = symC
        ident = identC / seqNC * 100


    if tablas:
        showMatrix(matriz, s1, s2)
    print('Identity = %2.1f percent' % ident)
    print('Score = %d\n' % seq_score)
    print(align1)
    print(sym)
    print(align2)
