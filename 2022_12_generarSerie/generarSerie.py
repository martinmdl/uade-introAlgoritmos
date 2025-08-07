# Previo diciembre 2022
# Ejercicio 1 – Serie con transformaciones
# Descripción:
#  Ingresar un número entero y positivo y generar la siguiente serie de valores:
# Si el valor es impar, multiplicarlo por 3 y sumarle 1.
# Si el valor es par, dividirlo por 2.
# Repetir este proceso hasta que el valor final sea 1.
# Ejemplo:
#  Si se ingresa el número 7, la secuencia generada será:
#  7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Requisitos del programa:
# * Guardar los valores obtenidos en una lista.
# * Informar cuántos valores se guardaron en la lista.
# * Determinar si hay valores primos en la lista y cuántos hay. Para esto, implementar una función que determine si un número es primo.
# * Mostrar la lista original con los valores separados por tres espacios.
# * Ordenar la lista de manera descendente y volverla a mostrar.
#
# Definición de número primo:
#  Un número es primo si es divisible solamente por 1 y por sí mismo.
#  Ejemplo: 5 es primo, pero 10 no lo es.

def es_natural(n):
    return n > 0 and n % 1 == 0

def es_primo(n):
    if n <= 1 or not es_natural(n):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def imprimir(lista):
    for i in range(len(lista)):
        print(lista[i], end="   ")

def ordenar_con_burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def main():
    num = -1
    secuencia = []
    while not es_natural(num):
        num = int(input("Ingrese entero positivo: "))

    secuencia.append(num)
    while num != 1:
        if num % 2 != 0:
            num = num * 3 + 1
        else:
            num = num // 2
        secuencia.append(num)

    print("Serie original:")
    imprimir(secuencia)
    print(f'\nSe guardaron {len(secuencia)} valores')

    primos = 0
    for i in range(len(secuencia)):
        if es_primo(secuencia[i]):
            primos += 1

    if primos == 0:
        print("No hay primos en la secuencia")
    else:
        print(f'Hay {primos} primos en la secuencia')

    ordenar_con_burbuja(secuencia)
    imprimir(secuencia)

if __name__ == "__main__":
    main()