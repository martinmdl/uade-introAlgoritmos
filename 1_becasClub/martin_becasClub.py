# Final Regular - 20/12/2024
#  Profesora: Anabella Baer
# Ejercicio:
#  Un club tiene un programa de becas y, entre otras cosas, requiere un programa para poder determinar la cantidad
#  de aspirantes que tienen para ese año.
# Condiciones: Las edades permitidas para las becas son de 13 a 50 años inclusive.
# Se requiere lo siguiente:
# 1) Leer por teclado las edades y el número de socio (4 dígitos, no repetidos) de los aspirantes a las becas.
# La lectura finaliza cuando se ingresa un número de socio igual a -1.
# 2) Determinar cuántos aspirantes a becas válidos hay e imprimir el resultado.
# 3) Determinar cuántos aspirantes no aplicaban para la beca por la edad.
# 4) Imprimir por pantalla el número de socio de cada uno y el número total.
# 5) Imprimir la lista total de aspirantes con sus edades y números de socio tal como fue cargada.
# Luego, volver a imprimirla ordenada de menor a mayor por número de socio.
# Utilizar al menos una función (además de la de ordenamiento) para resolver el enunciado.
#
# Validaciones:
# * El programa debe realizar todas las validaciones necesarias en la lectura y procesamiento de datos.
# Se dispone de la siguiente función de ordenamiento genérico por burbujeo para utilizar en la resolución del enunciado. En caso de ser necesario, adaptarla a las necesidades del problema
# Función de ordenamiento genérico por burbujeo

def existe(numSocio, lista):
    for fila in lista:
        if fila and fila[0] == numSocio:
            return True
    return False

def ingresarAspirantes():

    listaAspirantes = []

    while True:

        while True:
            numSocio = int(input("Ingresar nro socio: "))
            if numSocio >= 1000 and numSocio <= 9999 and not existe(numSocio, listaAspirantes):
                break
            elif numSocio == -1:
                return listaAspirantes
            print("Error: deben ser 4 dígitos y no ser repetido")

        while True:
            edad = int(input("Ingresar edad: "))
            if edad >= 0 and edad <= 120:
                break
            print("Error: edad fuera de rango")

        listaAspirantes.append([numSocio, edad])

def cumpleEdad(edad):
    return edad >= 13 and edad <= 50

def aspirantesValidos(aspirantes):

    contadorValidos = 0

    for fila in aspirantes:
        if fila and cumpleEdad(fila[1]):
            contadorValidos += 1

    rechazosPorEdad = len(aspirantes) - contadorValidos

    return contadorValidos, rechazosPorEdad

def ordenarMenorAMayor(lista):
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenada = True

def main():

    aspirantes = ingresarAspirantes()

    validos, rechazados = aspirantesValidos(aspirantes)

    print("\nAspirantes \t| Socio \t| Edad")
    for i in range(len(aspirantes)):
        print(f"{i}° \t\t| {aspirantes[i][0]} \t\t| {aspirantes[i][1]}")

    print(f"\nTotal aspirantes: {len(aspirantes)}")
    print(f"Aspirantes válidos: {validos}")
    print(f"Aspirantes rechazados por edad: {rechazados}")

    ordenarMenorAMayor(aspirantes)

    print(f"\nLista ordenada de menor a mayor:")
    print("\nAspirantes \t| Socio \t| Edad")
    for i in range(len(aspirantes)):
        print(f"{i}° \t\t| {aspirantes[i][0]} \t\t| {aspirantes[i][1]}")

if __name__ == "__main__":
    main()