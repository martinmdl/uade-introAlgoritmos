# Maratón 100k

import random


def cargarvalores(c):
    participantes = []
    canti = 0
    while canti < c:
        part = int(input("Ingresa el número del participante: "))
        # Verificar si el número ya está en la lista sin usar `repetido`
        i = 0
        while i < len(participantes):  # Recorremos la lista
            while participantes[i] == part:
                print(f"El participante {part} ya fue ingresado. Intenta con otro número.")
                part = int(input("Ingresa el número del participante: "))
            i += 1
        if i == len(participantes):  # Si el número no fue encontrado, lo agregamos
            participantes.append(part)
            print(f"Participante {part} cargado correctamente.")
            canti += 1  # Solo incrementamos si es un número nuevo
    return participantes


def cargartiempos(participantes):
    tiempo = []
    for i in range(len(participantes)):  # Generación manual de tiempos aleatorios
        tiempo.append(random.randint(0, 10000))
    return tiempo


def sumartiempos(tiempos):
    suma = 0
    for i in range(len(tiempos)):
        suma += tiempos[i]  # Sumamos los tiempos de los participantes
    return suma


def unirlistas(participantes, tiempos):
    lista_unida = []
    for i in range(len(participantes)):  # Une los valores manualmente
        lista_unida.append((participantes[i], tiempos[i]))
    return lista_unida


def busqueda_secuencial(lista_unida, numero):
    i = 0
    while i < len(lista_unida):
        if lista_unida[i][0] == numero:  # Comparar con el número del participante
            return lista_unida[i][1]  # Retorna el tiempo del participante si lo encuentra
        i += 1
    return -1  # Retorna -1 si no se encuentra el participante


def seleccion(lista_unida):
    n = len(lista_unida)
    # Ordenamiento por el método de selección
    for i in range(n):
        min_index = i  # Empezamos con el índice más bajo
        for j in range(i + 1, n):  # Buscamos el valor más pequeño en el resto de la lista
            if lista_unida[j][1] < lista_unida[min_index][1]:  # Comparamos por los tiempos
                min_index = j
        # Intercambiamos el valor más pequeño encontrado con el valor en la posición actual
        lista_unida[i], lista_unida[min_index] = lista_unida[min_index], lista_unida[i]


def mostrar_resultados(lista_unida):
    print("\nParticipantes y sus tiempos:")
    for i in range(len(lista_unida)):  # Usamos el índice para recorrer la lista
        participante = lista_unida[i][0]
        tiempo = lista_unida[i][1]
        print(f"Participante {participante}: {tiempo} segundos")


def main():
    # Entrada de cantidad de participantes
    cargar = int(input("Ingresa la cantidad de participantes que van a correr la carrera: "))

    # Carga de participantes y tiempos
    cargo = cargarvalores(cargar)
    tiempos = cargartiempos(cargo)

    # Unión de listas()`
    resultado = unirlistas(cargo, tiempos)

    # Mostrar resultados antes de ordenar
    mostrar_resultados(resultado)

    # Ordenamos los participantes por tiempo usando el método de selección
    seleccion(resultado)

    # Mostrar resultados después de ordenar
    mostrar_resultados(resultado)

    # Búsqueda de un participante
    buscar = int(input("\nIngresa el número del participante a buscar: "))
    tiempo_encontrado = busqueda_secuencial(resultado, buscar)

    if tiempo_encontrado != -1:
        print(f"\nEl participante {buscar} tiene un tiempo de {tiempo_encontrado} segundos.")
    else:
        print("\nParticipante no encontrado.")

    sumatoria = sumartiempos(tiempos)
    promedio_carrera = sumatoria / cargar

    print(f'El tiempo promedio de la carrera ha sido de: {promedio_carrera}')

if __name__ == "__main__":
    main()