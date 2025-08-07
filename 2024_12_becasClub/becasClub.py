# Final Regular - 20/12/2024
#  Profesora: Anabella Baer
# Ejercicio:
#  Un club tiene un programa de becas y, entre otras cosas, requiere un programa para poder determinar la cantidad
#  de aspirantes que tienen para ese año.
# Condiciones: Las edades permitidas para las becas son de 13 a 50 años inclusive.
# Se requiere lo siguiente:
# 1) Leer por teclado las edades y el número de socio (4 dígitos, no repetidos) de los aspirantes a las becas.
# La lectura finaliza cuando se ingresa un número de socio igual a -1.
# 2) Determinar cuántos aspirantes a becas válidos hay e imprimir el resultado.
# 3) Determinar cuántos aspirantes no aplicaban para la beca por la edad.
# 4) Imprimir por pantalla el número de socio de cada uno y el número total.
# 5) Imprimir la lista total de aspirantes con sus edades y números de socio tal como fue cargada.
# Luego, volver a imprimirla ordenada de menor a mayor por número de socio.
# Utilizar al menos una función (además de la de ordenamiento) para resolver el enunciado.
#
# Validaciones:
# * El programa debe realizar todas las validaciones necesarias en la lectura y procesamiento de datos.
# Se dispone de la siguiente función de ordenamiento genérico por burbujeo para utilizar en la resolución del enunciado. En caso de ser necesario, adaptarla a las necesidades del problema
# Función de ordenamiento genérico por burbujeo
def metodo_intercambio(lista1, lista2):
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(lista1) - 1):
            if lista1[i] > lista1[i + 1]:
                lista1[i], lista1[i + 1] = lista1[i + 1], lista1[i]
                lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]
                desordenada = True


def existe(lSocios, dato):
    for i in range(len(lSocios)):
        if lSocios[i] == dato:
            return True
    return False

def cargar_aspirantes(lSocios, lEdades):
    socio = int(input("Ingrese nro de socio (4 digitos): "))
    while socio != -1:
        while socio < 1000 or socio > 9999 or existe(lSocios, socio):
            socio = int(input("Error. Ingrese nro de socio (4 digitos): "))
            if socio == -1:
                break
        if socio == -1:
            break

        edad = int(input("Ingrese edad: "))
        while edad < 0 or edad > 100:
            edad = int(input("Ingrese edad (entre 0 y 100): "))

        lSocios.append(socio)
        lEdades.append(edad)
        socio = int(input("Ingrese nro de socio (4 digitos): "))

def validos(lEdades):
    aspirantes = 0
    rechazados = 0
    for i in range(len(lEdades)):
        if 13 <= lEdades[i] <= 50:
            aspirantes += 1
        else:
            rechazados += 1
    print(f'Hay {aspirantes} aspirantes y {rechazados} rechazados por edad')

def imprimir(lSocios, lEdades):
    print("SOCIO\tEDAD\t")
    for i in range(len(lEdades)):
        print(f'{lSocios[i]}\t{lEdades[i]}')

def main():
    socios = []
    edades = []
    cargar_aspirantes(socios, edades)

    validos(edades)

    print(f"\nTotal de aspirantes cargados: {len(socios)}")

    imprimir(socios, edades)

    print("Lista ordenada: ")
    metodo_intercambio(socios, edades)
    imprimir(socios, edades)

if __name__ == "__main__":
    main()