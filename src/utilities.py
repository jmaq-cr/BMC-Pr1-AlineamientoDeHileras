from copy import deepcopy

def cargarHilera():
    texto = ""
    tipo = str(input("1. Texto\n2. Archivo\n>>"))
    if tipo == "1":
        texto = str(input("Ingrese su cadena:\n>>"))
        return texto
    elif tipo == "2":
        direc = str(input("Ingrese la dirección de su archivo:\n>>"))
        try:
            file = open(direc,"r")
            texto = file.read()
            return texto
        except:
            print("Dirección no encontrada")
    else:
        print ("Opción no válida")
        return texto

def crearMatriz(m,n):
    matrixHeigth = (m*2)-1
    matrixWidth = (n*2)-1
    matrix = []

    for i in range(matrixHeigth):
        matrix.insert(i, [])
        for j in range(matrixWidth):
            if i%2 == 0 and j%2 == 0:
                matrix[i].insert(j, 0)
            else:
                matrix[i].insert(j, "·")
    return matrix


def showMatrix(matrix,seq1,seq2):
    printable = deepcopy(matrix)
    header1 = []
    cont1 = 0
    cont2 = 0

    for i in range(len(matrix)):
        if i%2 == 0 and i != 0:
            printable[i].insert(0, seq1[cont1])
            cont1 += 1
        elif i%2 == 0 and i == 0:
            printable[i].insert(0, "·")
        else:
            printable[i].insert(0, "·")

    for i in range(len(printable[0])):
        if i%2 != 0 and i != 1:
            header1.insert(i, seq2[cont2])
            cont2 += 1
        elif i%2 != 0 and i == 1:
            header1.insert(i, "·")
        else:
            header1.insert(i, "·")

    printable.insert(0,header1)

    for i in range(len(printable)):
        buffer = ""
        for j in range(len(printable[i])):
            buffer += "\t"+str(printable[i][j])
        print(buffer)


def addDirection(matrix, x, y, dir):
    xpos = x*2
    ypos = y*2
    if dir == "diag":
        matrix[xpos-1][ypos-1] = "\ "
    elif dir == "left":
        matrix[xpos][ypos - 1] = "- "
    else:
        matrix[xpos-1][ypos] = "| "
    return matrix

def setValue(matrix,x,y,val):
    xpos = x * 2
    ypos = y * 2
    matrix[xpos][ypos] = val
    return matrix

def getValue(matrix,x,y):
    xpos = x * 2
    ypos = y * 2
    return matrix[xpos][ypos]