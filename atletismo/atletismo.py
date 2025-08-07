# Competencia de Atletismo
# Desarrollar un programa en Python que permita gestionar la información de una competencia de atletismo.
# Requisitos:
# 1) Ingreso de datos - Permitir al usuario ingresar corredores con:
# * Un número único de identificación (entero positivo, sin repetirse).
# * Un tiempo en segundos (número positivo, puede ser decimal).
#
# 2) Cálculos a realizar:
# * Calcular y mostrar el tiempo total de todos los corredores.
# * Calcular y mostrar el porcentaje de tiempo que representa cada corredor respecto al total.
# * Ordenamiento y visualización:
#
# 3) Ordenar la lista de corredores de menor a mayor tiempo.
# * Mostrar el número del corredor y su tiempo.
# * Búsqueda de corredor:
#
# 4) Permitir al usuario buscar un corredor por su número de identificación.
# * Si el número existe, mostrar su tiempo.
# * Si el número no existe, mostrar un mensaje de error y volver a pedir un número válido.
#
# Consideraciones:
# * Validar que los números de identificación no se repitan.
# * Validar que los tiempos ingresados sean valores positivos.
# * Usar estructuras de datos adecuadas (listas paralelas o diccionarios).
# * Mostrar los resultados de forma clara y ordenada.


def ya_existe(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return True
    return False

def cargar_datos(lCorredores, lTiempos):
    idCorredor = 0
    while idCorredor != -1:
        idCorredor = int(input("Ingrese numero de corredor: "))
        while (idCorredor != -1 and idCorredor <= 0) or ya_existe(lCorredores, idCorredor):
            print("id inválido. Debe ser positivo o -1 para finalizar")
            idCorredor = int(input("Ingrese numero de corredor: "))

        if idCorredor == -1:
            break

        tiempo = float(input("Ingrese tiempo en segundos: "))
        while tiempo <= 0:
            tiempo = float(input("Ingrese tiempo en segundos: "))

        lCorredores.append(idCorredor)
        lTiempos.append(tiempo)

def seg_to_time(seg):
    h = seg // 3600
    m = (seg % 3600) // 60
    s = seg % 60
    print(f'- tiempo: {h:02.0f}:{m:02.0f}:{s:02.0f}')

def imprimir(lCorredores, lTiempos):
    for i in range(len(lCorredores)):
        print("id: ", lCorredores[i], end=" ")
        seg_to_time(lTiempos[i])

def total(lTiempos):
    tiempoTot = 0
    for i in range(len(lTiempos)):
        tiempoTot += lTiempos[i]
    return tiempoTot

def porcentaje_por_corredor(lTiempos):
    tiempoTot = total(lTiempos)
    for i in range(len(lTiempos)):
        porcentaje = (lTiempos[i] / tiempoTot) * 100
        print(f"Corredor {i + 1}: {porcentaje:.2f}% del tiempo total")

def ordenar_burbujeo(lCorredores, lTiempos):
    largo = len(lCorredores) 
    desordenada = True 
    while desordenada: 
        desordenada = False  
        for i in range(largo - 1): 
            if lTiempos[i] > lTiempos[i + 1]:  # ASCENDENTE
                lTiempos[i], lTiempos[i + 1] = lTiempos[i + 1], lTiempos[i]
                lCorredores[i], lCorredores[i + 1] = lCorredores[i + 1], lCorredores[i]
                desordenada = True 

def busqueda_lineal(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1

def main():
    corredores = []
    tiempos = []
    cargar_datos(corredores, tiempos)

    imprimir(corredores, tiempos)
    tiempoTotal = total(tiempos)
    print(f'Tiempo total entre todos: ', seg_to_time(tiempoTotal))

    porcentaje_por_corredor(tiempos)

    ordenar_burbujeo(corredores, tiempos)

    N = int(input("Ingrese numero de corredor a buscar: "))
    while not ya_existe(corredores, N):
        print("Ese corredor no existe")
        N = int(input("Ingrese numero de corredor a buscar: "))

    index = busqueda_lineal(corredores, N)
    print(f'El tiempo del corredor {N} es de', end=" ")
    seg_to_time(tiempos[index])

if __name__ == "__main__":
    main()