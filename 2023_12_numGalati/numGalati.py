# Examen Previo Diciembre 2023
# Ingresar por teclado la cantidad de valores para cargar a una lista, debiendo estar éste entre 20 y 30. Validar.
# Completar la lista con la cantidad ingresada de valores aleatorios entre 100 y 3000,
# debiendo ser números de Galati, y además, no deben estar repetidos.
#
# * Deberá utilizar funciones para determinar si están repetidos o si son de Galati,
# y la carga en la lista se hará en el programa principal.
# * Ordenar la lista por el metodo de Seleccion, de menor a mayor.
# * Mostrar los valores de la lista ordenada separada por 3 espacios.
# * Ingresar un valor por teclado. Informar si el valor se encuentra en la lista y en qué posición (Búsqueda Binaria).
#
# Nro de Galati: Son todos los numeros que se obtienen sumando numeros consecutivos anteriores al numero,
# comenzando desde 2. Por ejemplo, algunos números de Galati son:
# 9 = 2 + 3 + 4
# 20 = 2 + 3 + 4 + 5 + 6
# 104 = 2 + 3 + 4 + 5 + 6 + 7 +8 + 9 + 10 + 11 + …
import random


def es_galati(num):
    suma = 0
    for i in range(2, num):
        suma += i
        if suma == num:
            return True
        elif suma > num:
            break
    return False

def esta_repetido(lista, dato):
    repetido = False
    for i in range(len(lista)):
        if lista[i] == dato:
            repetido = True
            break
    return repetido

def ordenar_seleccion(lista):
    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[j] < lista [i]:
                lista[j], lista[i] = lista[i], lista[j]

def busqueda_binaria(lista, dato):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            return centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return -1

def imprimir_lista(lista):
    print("[", end="")
    for i in range(len(lista)):
        print(lista[i], end="   ")
    print("]", end="")

def main():
    N = int(input("Ingrese cantidad de valores: "))
    while N < 20 or N > 30:
        N = int(input("Ingrese cantidad de valores (20-30): "))

    numeros = []
    for i in range(N):
        numero = random.randint(100, 3000)
        while not es_galati(numero) or esta_repetido(numeros, numero):
            numero = random.randint(100, 3000)
        numeros.append(numero)

    print("Lista sin ordenar: ", numeros)

    ordenar_seleccion(numeros)

    print("Lista  con espacios: ", end="")
    imprimir_lista(numeros)

    buscado = int(input("\nIngrese un numero a buscar(100-3000): "))
    while buscado < 100 or buscado > 3000:
        buscado = int(input("Ingrese un numero a buscar(100-3000): "))
    indice = busqueda_binaria(numeros, buscado)

    if indice == -1:
        print(f'{buscado} no encontrado')
    else:
        print(f'{buscado} esta en la posicion {indice}')

if __name__ == "__main__":
    main()