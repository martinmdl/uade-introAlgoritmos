# Noviembre 2023
# Ingresar por teclado, y cargar en una lista, números comprendidos entre -255 y 255, que no se repitan
# y que sean números malvados. El fin de ingreso se indica con -1. Que no se repita y que sea malvado,
# deberá resolverlo con una función para cada ítem.
# Mostrar la lista obtenida
# Ordenar la lista por el Metodo de Burbujeo
# Mostrar la lista obtenida con los valores separados por 3 espacios
# Ingresar un valor por teclado y buscarlo en la lista por el metodo de la Búsqueda Binaria.
# Informar si el dato se encuentra o no en la lista. Si está, informar en qué posición se encuentra.
#
# Número Malvado: es número entero y positivo, que contiene cantidad par de 1 en su forma binaria, por ej:
# 243 = 11110011
# 255 = 11111111
# 102 = 1100110

def es_natural(num):
    return num > 0 and num % 1 == 0

def to_binary(n):
    bin = []
    if n == 0:
        return [0]
    else:
        while n > 0:
            bin.append(n % 2)
            n = n // 2

        # ahora tengo el binario pero al reves, lo doy vuelta apra que me quede pero no hace falta
        binario = []
        for i in range(len(bin) -1, -1, -1):
            binario.append(bin[i])
        return binario

def cantidad_unos(binList):
    unos = 0
    for bit in binList:
        if bit == 1:
            unos += 1
    return unos

def es_malvado(num):
    return es_natural(num) and cantidad_unos(to_binary(num)) % 2 == 0

def se_repite(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return True
    return False

def burbujeo(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista) -1 -i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

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

def imprimir_espacios(lista):
    print("[", end="")
    for i in range(len(lista)):
        print(lista[i], end="   ")
    print("]", end="")

def main():
    listaNumeros = []
    numero = 0
    while numero != -1:
        numero = int(input("Ingrese numero (-255 a 255). Finalice con -1: "))

        while numero < -255 or numero > 255:
            numero = int(input("Error. Ingrese numero (-255 a 255). Finalice con -1: "))

        if numero == -1:
            break

        if es_malvado(numero) and not se_repite(listaNumeros, numero):
            listaNumeros.append(numero)

    print("Lista no ordenada: ", listaNumeros)
    print("Lista ordenada:", end="")
    burbujeo(listaNumeros)
    imprimir_espacios(listaNumeros)

    buscado = int(input("\nIngrese un numero a buscar(-255 a 255): "))
    while buscado < -255 or buscado > 255:
        buscado = int(input("Ingrese un numero a buscar(-255 a 255): "))
    indice = busqueda_binaria(listaNumeros, buscado)

    if indice == -1:
        print(f'{buscado} no encontrado')
    else:
        print(f'{buscado} esta en la posicion {indice}')


if __name__ == "__main__":
    main()