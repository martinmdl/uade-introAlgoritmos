# Final Adelantado - 29/11/2024
#  Profesor: Manuel Adrián Cáceres
# Ejercicio 1 (1,5 puntos + 0,5 puntos por uso de funciones con parámetros)
#  Análisis de Ventas Diarias: Desarrolla un programa en Python que simule la generación de una lista de
#  30 números enteros aleatorios, cada uno representando ventas diarias en un rango entre 50 y 500 unidades.
# El programa debe:
# Imprimir todos los días en que las ventas estuvieron por debajo de 150 unidades.
# Calcular e imprimir la cantidad promedio de ventas (sin usar funciones predefinidas como sum o len).
# Restricciones:
#  ✅ No se permite el uso de las funciones predefinidas de Python como min, max, sum, len ni listas por comprensión.
#  ✅ La lógica debe ser implementada manualmente.
import random

def cargar_ventas(ventas):
    for i in range(30):
        ventas.append(random.randint(50, 500))

def promedio(lista):
    suma = 0
    total = 0
    for i in range(len(lista)):
        suma += lista[i]
        total += 1
    return suma / total

def debajo_150(lista):
    debajo = []
    debajoDias = []
    for i in range(len(lista)):
        if lista[i] < 150:
            debajo.append(lista[i])
            debajoDias.append(i)
    return debajo, debajoDias

def imprimir(lista1, lista2):
    for i in range(len(lista1)):
        print(f'Día {lista2[i] + 1} - {lista1[i]} unidades')

def main():
    ventas = []
    cargar_ventas(ventas)
    print(f'Ventas: {ventas}')

    avg = promedio(ventas)
    print(f'Promedio: {avg:.2f}')

    bajo, bajoDias = debajo_150(ventas)
    print(f'Dias debajo de 150 unidades')
    imprimir(bajo, bajoDias)

if __name__ == "__main__":
    main()