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

vendedores = []
ventas = []

def cuatro_digitos(n):
    if n < 0:
        n = -n
    return 1000 <= n <= 9999

def busqueda_secuencial_indice(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1

def imprimir(listaVendedores, listaImportes):
    for i in range(len(listaVendedores)):
        print(f'Vendedor {listaVendedores[i]} : ${listaImportes[i]}')

def ordenar_burbuja(lista1, lista2):
    largo = len(lista1)
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo - 1):
            if lista2[i] < lista2[i+1]:
                lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]
                lista1[i], lista1[i + 1] = lista1[i + 1], lista1[i]
                desordenada = True


def buscar_maximo(listaVentas, listaVendedores):
    max = 0
    idVendedor = -1
    for i in range(len(listaVentas)):
        if listaVentas[i] > max:
            max = listaVentas[i]
            idVendedor = listaVendedores[i]
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

        indice_en_lista = busqueda_secuencial_indice(vendedores, idVendedor)
        if indice_en_lista != -1:
            ventas[indice_en_lista] += importe
        else:
            vendedores.append(idVendedor)
            ventas.append(importe)

    print("\nVendedores (sin ordenar): ")
    imprimir(vendedores, ventas)

    print("\nVendedores (ordenados): ")
    ordenar_burbuja(vendedores, ventas)
    imprimir(vendedores, ventas)

    buscar_maximo(ventas, vendedores)


if __name__ == "__main__":
    main()