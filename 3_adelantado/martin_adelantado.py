import random

######################### PUNTO 1 #########################

def promedio(lista):
    acum = 0
    cont = 0

    for i in lista:
        acum += i
        cont += 1

    return acum / cont

def punto1():
    ventasTotales = []

    for dia in range(1,31):
        ventasTotales.append(random.randint(50,500))

        if ventasTotales[dia-1] < 150:
            print(f"Dia {dia}: {ventasTotales[dia-1]}")

    print(f"\nPromedio total de ventas: {promedio(ventasTotales):.1f}\n{ventasTotales}")

######################### PUNTO 2 #########################

def punto2():

    animalesLargos = []
    animales = ["perro", "gato", "elefante", "hipopótamo", "jirafa", "lobo", "zorro", "delfín", "pingüino", "cocodrilo", "ornitorrinco", "canguro", "caballo", "mono", "águila"]

    for animal in animales:
        contadorLetras = 0
        for letra in animal:
            contadorLetras += 1
        if contadorLetras > 8:
            animalesLargos.append(animal)

    print(f"Animales con mas de 8 letras: {animalesLargos}")

    for i in range(largo(animalesLargos)-1):
        if animalesLargos[i] > animalesLargos[i+1]:
            aux = animalesLargos[i]
            animalesLargos[i] = animalesLargos[i+1]
            animalesLargos[i+1] = aux

    print(f"Ordeno alfabeticamente: {animalesLargos}")


######################### PUNTO 3 #########################

def printArr(arr):
    for i in range(5):
        print(f"{arr[i]}")
    print("\n")

def largo(lista):
    cont = 0
    for _ in lista:
        cont += 1
    return cont

def crearArr():
    arr = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(random.randint(10, 50))
        arr.append(row)
    return arr

def punto3():
    arr1 = crearArr()
    arr2 = crearArr()
    arr3 = crearArr()
    cont = 0
    acum = 0

    for i in range(5):
        for j in range(5):
            arr3[i][j] = arr1[i][j] + arr2[i][j]
            if i == j:
                cont += 1
                acum += arr3[i][j]

    printArr(arr1)
    printArr(arr2)
    printArr(arr3)
    print(f"Promedio diagonal: {acum / cont}")
        

######################### PUNTO 4 #########################

def ordenamiento_intercambio_desc(matriz):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(matriz) - 1):
            if matriz[i][3] < matriz[i+1][3]:
                aux = matriz[i+1]
                matriz[i+1] = matriz[i]
                matriz[i] = aux
                desordenado = True
    return matriz

def punto4():

    productos = [
        [1, "Laptop", 1200.50],
        [2, "Mouse", 15.75],
        [3, "Teclado", 35.20],
        [4, "Monitor", 250.00],
        [5, "Impresora", 180.99]
    ]

    productos1 = productos

    for i in range(len(productos1)):
        productos1[i].append(round((productos1[i][2] * 1.2), 2))

    ordenamiento_intercambio_desc(productos1)

    printArr(productos)
    printArr(productos1)

#########################   RUN   #########################

def main():
    print("\n\n### PUNTO 1 ###\n")
    punto1()
    print("\n\n### PUNTO 2 ###\n")
    punto2()
    print("\n\n### PUNTO 3 ###\n")
    punto3()
    print("\n\n### PUNTO 4 ###\n")
    punto4()

if __name__ == "__main__":
    main()