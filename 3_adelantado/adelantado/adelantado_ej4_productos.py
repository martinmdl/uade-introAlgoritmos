# Ejercicio 4 (2 puntos + 0,5 por uso de funciones con parámetros + 0,5 por uso de algoritmo de ordenamiento de selección)
#  Gestión de Productos y Precios de Venta: Crear una matriz con datos de prueba que contenga:
# Columna 1: ID del producto.
# Columna 2: Nombre del producto.
# Columna 3: Precio de compra.

# El programa debe:
# Calcular el precio de venta para cada producto, incrementando el precio de compra en un 20%.
# Crear una nueva matriz igual a la anterior, pero agregando una cuarta columna con el precio de venta.
# Ordenar la nueva matriz por la columna del precio de venta, utilizando el algoritmo de burbuja (Bubble Sort).
# Imprimir ambas matrices (la original y la nueva ordenada).

def precio_compra(m):
    for i in range(len(m)):
        m[i].append(m[i][2] * 1.2)

def imprimir(m):
    # Esta función imprime la matriz con los datos
    print()
    print("ID\tProducto\tPrecio Compra\tPrecio Venta")
    for i in range(len(m[0])):  # Imprimir por producto
        print(f'{m[0][i]}\t\t{m[1][i]}\t\t{m[2][i]}\t\t{m[3][i]}')

def ordenar_burbuja(m):
    largo = len(m)
    for i in range(largo - 1):
        for j in range(largo - i - 1):
            if m[j][3] > m[j + 1][3]:
                m[j], m[j + 1] = m[j + 1], m[j]

def main():
    matriz = [
        [1000, "Harina", 300],
        [1002, "Manzana", 400],
        [1003, "Huevos", 5000],
        [1004, "Tomates", 1000],
        [1005, "Nueces", 6000],
        [1006, "Papa", 2500],
        [1007, "Arroz", 800],
        [1008, "Quinoa", 3100],
        [1009, "Azucar", 1850],
        [1010, "Peras", 750]
    ]

    precio_compra(matriz)

    imprimir(matriz)

    ordenar_burbuja(matriz)

    imprimir(matriz)

if __name__ == "__main__":
    main()

