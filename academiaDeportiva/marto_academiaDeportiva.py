# Título: Gestión de Aspirantes en una Academia Deportiva Multidisciplinaria

# Descripción:

# Se te solicita desarrollar un programa en Python para administrar la información de los aspirantes 
# a una academia deportiva que ofrece cuatro disciplinas: fútbol, natación, voleibol y handball. El programa deberá realizar las siguientes tareas:

# Generación de Datos: 

# Permitir al usuario ingresar la cantidad de aspirantes (entre 100 y 500). 
# Generar aleatoriamente los datos de cada aspirante, incluyendo: 
# DNI (número entero aleatorio entre 400.000 y 60.000.000). 
# Edad (número entero aleatorio entre 12 y 80). 
# Deporte de interés (número entero aleatorio entre 1 y 4, donde 1 representa fútbol, 2 natación, 3 voleibol y 4 handball). 

# Clasificación por Deporte:

# Crear listas separadas para cada deporte, almacenando los DNIs de los aspirantes según su elección. 
# Imprimir en pantalla los DNIs de los aspirantes de cada deporte. 

# Resumen por Deporte:

# Calcular e imprimir un resumen ordenado descendentemente por la cantidad de aspirantes en cada deporte, incluyendo: 
# Nombre del deporte. 
# Cantidad de aspirantes. 
# Promedio de edad de los aspirantes. 


# | IMPORTACIÓN |
from random import randint

def ordenarMayorAMenor(lista):
    return 2

def main():

    dnisFutbol = []
    acumEdadFutbol = 0
    dnisNatacion = []
    acumEdadNatacion = 0
    dnisVoleibol = []
    acumEdadVoleibol = 0
    dnisHandball = []
    acumEdadHandball = 0

    while True:
        cantAspirantes = int(input("Ingrese cantidad de aspirantes (entre 100 y 500): "))
        if cantAspirantes >= 100 and cantAspirantes <= 500:
            break
        print("Error: ingresar entre 100 y 500 aspirantes")

    for i in range(cantAspirantes):

        aspirante = []

        aspirante.append(randint(400000, 60000000))
        aspirante.append(randint(12, 80))
        aspirante.append(randint(1, 4))

        # aspirantes.append(aspirante)

        if aspirante[2] == 1:
            dnisFutbol.append(aspirante[0])
            acumEdadFutbol += aspirante[1]
        elif aspirante[2] == 2:
            dnisNatacion.append(aspirante[0])
            acumEdadNatacion += aspirante[1]
        elif aspirante[2] == 3:
            dnisVoleibol.append(aspirante[0])
            acumEdadVoleibol += aspirante[1]
        else:
            dnisHandball.append(aspirante[0])
            acumEdadHandball += aspirante[1]

    acumEdad = acumEdadFutbol + acumEdadNatacion + acumEdadVoleibol + acumEdadHandball
    promedioEdad = acumEdad / cantAspirantes

    print(f"\n## FÚTBOL ##\n{dnisFutbol}\n")
    print(f"\n## NATACIÓN ##\n{dnisNatacion}\n")
    print(f"\n## VOLLEY ##\n{dnisVoleibol}\n")
    print(f"\n## HANDBALL ##\n{dnisHandball}\n")

    aspirantes = [dnisFutbol, dnisNatacion, dnisVoleibol, dnisHandball]
    ordenarMayorAMenor(aspirantes)

    print(f"\n## RESUMEN ##")
    print(f"\t- FÚTBOL: aspirantes = {len(dnisFutbol)} | Edad promedio: {(acumEdadFutbol / len(dnisFutbol)):.2f}")
    print(f"\t- NATACIÓ: aspirantes = {len(dnisNatacion)} | Edad promedio: {(acumEdadNatacion / len(dnisNatacion)):.2f}")
    print(f"\t- VOLLEY: aspirantes = {len(dnisVoleibol)} | Edad promedio: {(acumEdadVoleibol / len(dnisVoleibol)):.2f}")
    print(f"\t- HANDBAL: aspirantes = {len(dnisHandball)} | Edad promedio: {(acumEdadHandball / len(dnisHandball)):.2f}")

if __name__ == "__main__":
    main()