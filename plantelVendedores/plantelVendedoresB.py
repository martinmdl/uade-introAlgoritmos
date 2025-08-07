# La empresa cuenta con un plantel de vendedores, numerados con valores positivos arbitrarios de cuatro dígitos.
# Por cada venta realizada se ingresa por teclado el número de vendedor y el importe de la misma,
# donde un número de vendedor -1 indica el final de los datos.
# Realizar un programa para imprimir:
# * Total vendido por cada vendedor, ordenado de mayor a menor según el total vendido
# * Importe y número de vendedor correspondiente a la mayor venta realizada
#
# Pistas:
# La cantidad de vendedores no se conoce. Este dato deberá deducirse de las ventas ingresadas.
# Debe verificarse que los números de vendedor tengan cuatro dígitos, rechazando los valores inválidos.
#
# Ejemplo:
# Total vendido por vendedor:
# Vendedor 1802: $ 320000
# Vendedor 9263: $ 59000
# La mayor venta la realizó el vendedor 4746 con $980000

matriz = [[], []]
# matriz[0] == vendedores

def cuatro_digitos(n):
    if n < 0:
        n = -n
    return 1000 <= n <= 9999

def busqueda_secuencial_indice(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1

def imprimir(mat):
    for i in range(len(mat[0])):
        print(f'Vendedor {mat[0][i]} : ${mat[1][i]}')

def ordenar_burbuja(mat):
    largo = len(mat[0])
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo - 1):
            if mat[1][i] < mat[1][i+1]:
                mat[1][i], mat[1][i + 1] = mat[1][i + 1], mat[1][i]
                mat[0][i], mat[0][i + 1] = mat[0][i + 1], mat[0][i]
                desordenada = True


def buscar_maximo(mat):
    max = 0
    idVendedor = -1
    for i in range(len(mat[1])):
        if mat[1][i] > max:
            max = mat[1][i]
            idVendedor = mat[0][i]
    print(f'\nLa mayor venta la realizó el vendedor {idVendedor} con ${max:.2f}')

def main():
    idVendedor = 0
    while idVendedor != -1:
        idVendedor = int(input("Ingrese id de vendedor, finalice con -1: "))
        while idVendedor != -1 and not cuatro_digitos(idVendedor):
            idVendedor = int(input("Ingrese id de vendedor (4 digitos): "))

        if idVendedor == -1:
            break

        importe = float(input(f'Ingrese importe venta vendedor id={idVendedor}: '))
        while importe < 0:
            importe = float(input(f'Importe no puede ser negativo.\nIngrese importe venta vendedor id={idVendedor}: '))

        indice_en_lista = busqueda_secuencial_indice(matriz[0], idVendedor)
        if indice_en_lista != -1:
            matriz[1][indice_en_lista] += importe
        else:
            matriz[0].append(idVendedor)
            matriz[1].append(importe)

    print("\nVendedores (sin ordenar): ")
    imprimir(matriz)

    print("\nVendedores (ordenados): ")
    ordenar_burbuja(matriz)
    imprimir(matriz)

    buscar_maximo(matriz)

if __name__ == "__main__":
    main()