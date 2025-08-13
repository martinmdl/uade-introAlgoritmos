# Ejercicio 3 (1,5 puntos + 0,5 por uso de funciones con parámetros)
#  Operaciones con Matrices y Diagonales:
# Generar dos matrices de 5 filas y 5 columnas, llenando cada una con números aleatorios entre 10 y 50.
# Sumar los valores correspondientes de las dos matrices, celda por celda (ejemplo: matriz1[4][4] + matriz2[4][4]),
# y guardar el resultado en una tercera matriz.
# Calcular el promedio de los elementos de la diagonal principal de la tercera matriz.
# Mostrar las tres matrices (las dos originales y la resultante) y el promedio calculado.
# Restricciones:
#  ✅ Usa funciones para separar la lógica de:
# Generación de matrices
# Suma de matrices
# Cálculo del promedio de la diagonal
#  ✅ Evita usar librerías como NumPy para garantizar la implementación manual de la lógica.
import random


def cargar_matriz():
    m = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(random.randint(10, 50))
        m.append(fila)
    return m

def sumar_matrices(m1, m2):
    m3 = []
    for i in range(5):
        suma = 0
        fila = []
        for j in range(5):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        m3.append(fila)
    return m3

def promedio_diag_principal(m):
    suma = 0
    count = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                suma += m[i][j]
                count += 1
    return suma / count

def promedio_diag_principal_simple(m):
    suma = 0
    for i in range(5):
        suma += m[i][i]
    return suma / 5

def imprimir(m):
    print()
    for i in range(5):
        for j in range(5):
            print(m[i][j], end="   ")
        print()

def main():
    mat1 = cargar_matriz()
    mat2 = cargar_matriz()

    print("Matriz 1: ")
    imprimir(mat1)

    print("Matriz 2: ")
    imprimir(mat2)

    mat3 = sumar_matrices(mat1, mat2)

    print("Matriz 3: ")
    imprimir(mat3)

    avg = promedio_diag_principal(mat3)
    print(f'El promedio de la diagonal principal es {avg}')


if __name__ == "__main__":
    main()