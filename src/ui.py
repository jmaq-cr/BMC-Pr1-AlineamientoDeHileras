from src.utilities import *


def main():
    salir = False

    match = 1
    mismatch = -1
    gap = -2

    secuencia1 = ""
    secuencia2 = ""

    while salir == False:
        print("1. Cargar Secuencia 1")
        print("2. Cargar Secuencia 2")
        print("3. Alineamiento Global")
        print("4. Alineamiento Local")
        print("5. Alineamiento Semiglobal")
        print("6. Alineamiento Global K-Band")
        opc = str(input(">>"))
        if opc == "1":
            secuencia1 = cargarHilera();
        elif opc == "2":
            secuencia2 = cargarHilera()
main()