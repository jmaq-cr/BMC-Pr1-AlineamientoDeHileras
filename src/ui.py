from src.globalalig import *
from src.semiglobal import *
from src.kband import *
from src.lineal import *
from src.local import *
from src.afinidadgap import *
import src.utilities



def main():
    salir = False

    secuencia1 = ""
    secuencia2 = ""

    while salir == False:
        print("1. Cargar Secuencia 1")
        print("2. Cargar Secuencia 2")
        print("3. Alineamiento Global")
        print("4. Alineamiento Local")
        print("5. Alineamiento Semiglobal")
        print("6. Alineamiento Global K-Band")
        print("7. Alineamiento Con Función de Afin de Costo por Gap")
        print("8. Alineamiento Global con Espacio Lineal")
        opc = str(input(">>"))
        if opc == "1":
            secuencia1 = cargarHilera()
        elif opc == "2":
            secuencia2 = cargarHilera()
        elif opc == "3":
            needle(secuencia1,secuencia2)
        elif opc == "4":
            water(secuencia1,secuencia2)
        elif opc == "5":
            semiglobal(secuencia1,secuencia2)
        elif opc == "6":
            k = str(input("Ingrese el tamaño de K"))
            if len(k) < len(secuencia1) and len(k) < len(secuencia2) and k.isdecimal():
                kBand(secuencia1,secuencia2,int(k))
            else:
                print("El tamaño de K no es válido")
        elif opc == "7":
            print("Hace la función afin de costo por gap")
        elif opc == "8":
            lineal(secuencia1,secuencia2)
        elif opc == "#ayuda":
            print("Imprime la ayuda")
        elif opc == "#tablas":
            if src.utilities.tablas == True:
                src.utilities.tablas = False
            else:
                src.utilities.tablas = True
            print(tablas)
        elif opc == "#listar":
            print("Alineamiento Global")
            print("Alineamiento Local")
            print("Alineamiento Semiglobal")
            print("Alineamiento Global K-Band")
            print("Alineamiento Con Función de Afin de Costo por Gap")
            print("Alineamiento Global con Espacio Lineal")
        elif opc == "#val":
            print(pt)
        elif opc == "#match":
            val = str(input("El valor actual de match es "+str(pt['match']) + " si lo desea cambiar ingréselo a continuación: "))
            if val != "" and val.lstrip("-").isdigit():
                src.utilities.pt['match'] = int(val)
            else:
                print("El valor no es correcto")
        elif opc == "#mismatch":
            val = str(input("El valor actual de mismatch es " + str(pt['mismatch']) + " si lo desea cambiar ingréselo a continuación: "))
            if val != "" and val.lstrip("-").isdigit():
                src.utilities.pt['mismatch'] = int(val)
            else:
                print("El valor no es correcto")
        elif opc == "#gap":
            val = str(input("El valor actual de gap es " + str(pt['gap']) + " si lo desea cambiar ingréselo a continuación: "))
            if val != "" and val.lstrip("-").isdigit():
                src.utilities.pt['gap'] = int(val)
                print(pt)
            else:
                print("El valor no es correcto")
        elif opc == "#salir":
            salir = True


