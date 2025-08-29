# PUNTO 1 – Carga de Series
# Desarrollar una función llamada cargaSeries(lSeries) que reciba una lista vacía y la complete con los códigos de las series clásicas disponibles en la plataforma.
# * Los códigos son números enteros entre 100 y 300, sin duplicados.
# * La cantidad total de series es de 110.
# * Para garantizar que no se repitan códigos, implementar una función busqueda() que permita verificar si un código ya está presente en la lista antes de agregarlo.
#
# PUNTO 2 – Registro de Votación
# Durante las últimas 10 semanas del año, la empresa lanza una encuesta para que los usuarios elijan:
# * Código de serie clásica (entero entre 100 y 300).
# * Número de fin de semana en que prefieren que se emita la serie (entero entre 1 y 10).
#
# Requisitos:
# * Validar ambos datos utilizando una función genérica llamada validaIngreso().
# * Si el código de serie ingresado no existe en el catálogo, mostrar el mensaje: ERROR, ¡SERIE INEXISTENTE!
# * Cada par de código + semana corresponde a un solo voto.
# * La carga de votos finaliza cuando se ingresa el código 99.
# * No se garantiza orden alguno en la entrada de los datos.
# * Conservar toda la información en memoria para su posterior análisis.
#
# PUNTO 3 – Total de Votos por Serie
# Implementar una función que reciba las estructuras correspondientes y emita un listado con el total de votos recibidos por cada serie,
# ordenado de mayor a menor según la cantidad de votos.
# Formato de salida:
# CÓDIGO DE SERIE      CANTIDAD DE VOTOS
# ---------------      ------------------
# 123                  45
# 256                  32
# ...                  ...
# TOTAL DE VOTOS RECIBIDOS: XXX
#
# PUNTO 4 – Series Sin Votos
# Desarrollar una función que muestre un listado con los códigos de series que no recibieron votos
# y el porcentaje que representan sobre el total del catálogo.
#
# Series sin votos: [145, 178, 199, ...]
# Porcentaje sobre el total: XX.XX %
import random

def busqueda(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1

def ordenar_burbuja(lista1, lista2):
    largo = len(lista1)
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo - 1):
            if lista2[i] < lista2[i + 1]:
                lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]
                lista1[i], lista1[i + 1] = lista1[i + 1], lista1[i]
                desordenada = True

def busqueda_binaria(lista, dato):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            return centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return -1


def cargaSeries(lSeries):
    N = 110
    for i in range(N):
        num = random.randint(100, 300)
        if busqueda(lSeries, num) == -1:
            lSeries.append(num)

def validaIngreso(lSeries, codigo, finde):
    # La validación será verdadera solo si:
    # - El código está en el rango [100, 300].
    # - El código de la serie existe en la lista.
    # - El fin de semana está en el rango [1, 10].
    return (100 <= codigo <= 300) and busqueda(lSeries, codigo) != -1 and (1 <= finde <= 10)

def cargaVotos(votos):
    N = 110
    for i in range(N):
        votos.append(0)

def imprimir(lSeries, lVotos):
    total = 0
    print("CODIGO DE SERIE\t\tCANTIDAD DE VOTOS")
    for i in range(len(lSeries)):
        if lVotos[i] != 0:
            print(f'{lSeries[i]}\t\t\t{lVotos[i]}')
            total += lVotos[i]

    print("TOTAL DE VOTOS RECIBIDOS: ", total)

def sin_votos(lSeries, lVotos):
    total_sin_votos = 0
    print("CODIGO DE SERIES SIN VOTOS")
    for i in range(len(lSeries)):
        if lVotos[i] == 0:
            print(f'{lSeries[i]}')
            total_sin_votos += 1

    porcentaje = total_sin_votos / len(lSeries) * 100
    print(f'Hay {total_sin_votos} de {len(lSeries)} series sin votos, que es el %{porcentaje}')

def main():
    series = []
    votos = []
    cargaSeries(series)
    cargaVotos(votos)
    print(series)

    codigo = 0
    while codigo != 99:
        codigo = int(input("Ingrese un código (100-300). Finalice con 99: "))

        if codigo == 99:
            break

        finde = int(input("Ingrese un número de fin de semana (1-10): "))

        while not validaIngreso(series, codigo, finde):
            print("ERROR! SERIE INEXISTENTE o FINDE NO EN RANGO")
            codigo = int(input("Ingrese un código (100-300). Finalice con 99: "))

            if codigo == 99:
                break

            finde = int(input("Ingrese un número de fin de semana (1-10): "))

        if codigo == 99:
            break

        index = busqueda(series, codigo)
        votos[index] += 1

    ordenar_burbuja(series, votos)
    imprimir(series, votos)
    sin_votos(series, votos)

if __name__ == "__main__":
    main()