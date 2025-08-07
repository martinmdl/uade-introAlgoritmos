# Facturación Mensual de un Club Deportivo
# Un club deportivo ofrece a sus socios múltiples actividades deportivas y culturales.
# Algunos socios solo pagan la cuota social sin adicionales.
# El club necesita calcular la facturación mensual.
# Estructura de facturación:
# * Solo cuota social: $2000
# * Hasta 2 actividades adicionales: $3000
# * De 3 a 5 actividades: $5000
# * Pase full (todas las actividades libres): $6000
# Requisitos del programa:
# 1. Leer por teclado el número total de socios (N).
# 2. Generar los números de socio de manera aleatoria (4 dígitos).
# 3. Mostrar en pantalla:
# - Cantidad total de socios.
# - Facturación total del mes.
# - Cantidad de socios por tipo de facturación.
# 4. Permitir que el usuario ingrese un número de socio y devolver la cuota correspondiente.

# Mis suposiones porque perdí el ej:
# Cada socio se genera con:
# * Un número aleatorio de 4 dígitos (random.randint(1000, 9999)).
# * Una cantidad de actividades entre 0 y, por ejemplo, 7 (también aleatorio).
# A partir de eso:
# * 0 actividades → $2000
# * 1-2 actividades → $3000
# * 3-5 actividades → $5000
# * 6 o más → $6000 (pase full)

import random


def existe(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return True
    return False


def cargar_socios(lSocios, lActividades, N):
    for i in range(N):
        idSocio = random.randint(1000,9999)
        while existe(lSocios, idSocio):
            idSocio = random.randint(1000, 9999)
        cantAct = random.randint(0, 10)
        lSocios.append(idSocio)
        lActividades.append(cantAct)

def facturacion_total(lActividades):
    total = 0
    for i in range(len(lActividades)):
        if lActividades[i] == 0:
            total += 2000
        elif lActividades[i] <= 2:
            total += 3000
        elif lActividades[i] <= 5:
            total += 5000
        else:
            total += 6000
    return total

def tipo_facturacion(lActividades):
    tipo0 = 0
    tipo1 = 0
    tipo2 = 0
    tipo3 = 0
    for i in range(len(lActividades)):
        if lActividades[i] == 0:
            tipo0 += 1
        elif lActividades[i] <= 2:
            tipo1 += 1
        elif lActividades[i] <= 5:
            tipo2 += 1
        else:
            tipo3 += 1
    print(f'Socios precio base ($2000): {tipo0}')
    print(f'Socios 1-2 actividades ($3000): {tipo1}')
    print(f'Socios 3-5 actividades ($5000): {tipo2}')
    print(f'Socios +5 actividades ($6000): {tipo3}')

def ordenar_burbuja(lista1, lista2):
    largo = len(lista1)
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(largo - 1):
            if lista2[i] > lista2[i + 1]:
                lista2[i], lista2[i + 1] = lista2[i + 1], lista2[i]
                lista1[i], lista1[i + 1] = lista1[i + 1], lista1[i]
                desordenada = True

def busq_bin(lista, dato):
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

def imprimir(lSocios, lAct):
    print("ID\t\tACT")
    for i in range(len(lSocios)):
        print(f'{lSocios[i]}\t{lAct[i]}')

def main():
    socios = []
    actividades = []
    N = int(input("Ingrese numero total de socios: "))
    while N < 0:
        N = int(input("Debe ser un numero positivo.\nIngrese numero total de socios: "))

    cargar_socios(socios, actividades, N)
    print(f'La cantidad total de socios es {len(socios)}')

    imprimir(socios, actividades)

    totalFacturado = facturacion_total(actividades)
    print(f'El total facturado es ${totalFacturado}')

    tipo_facturacion(actividades)

    idSoc = int(input("Ingresa numero de socio a buscar: "))
    while idSoc < 0 or idSoc < 1000 or idSoc > 9999:
        idSoc = int(input("Debe ser un numero positivo de 4 digitos.\nIngresa numero de socio a buscar: "))

    ordenar_burbuja(actividades, socios)

    print("\nOrdenados: ")
    imprimir(socios, actividades)

    index = busq_bin(socios, idSoc)
    match actividades[index]:
        case 0:
            print(f'Socio {idSoc} paga $2000')
        case 1 | 2:
            print(f'Socio {idSoc} paga $3000')
        case 3 | 4 | 5:
            print(f'Socio {idSoc} paga $5000')
        case _:
            print(f'Socio {idSoc} paga $6000')

    print(f'')


if __name__ == "__main__":
    main()