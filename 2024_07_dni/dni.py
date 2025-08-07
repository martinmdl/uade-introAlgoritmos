# Final Regular - Julio 2024
# Profesor: D’Aquino

# Objetivo:
# Ingresar su DNI y resolver los puntos indicados a continuación.

# Ejercicio:
# Ingreso del DNI:
# Ingrese su número de D.N.I. de la misma manera que ingresa la clave en un cajero automático.
# Si no lo recuerda, ingrese un número de 8 dígitos, entre 0 y 9, asegurándose de que el primer dígito no sea 0.
# Ejemplo válido: 45123951

# Transformación en lista:
# Crear una lista con los dígitos del número de DNI en orden inverso.
# Ejemplo: si el número ingresado es 45123951, la lista debe ser [1,5,9,3,2,1,5,4].

# Operaciones a realizar:
# - Controlar que el primer dígito ingresado no sea 0.
# - Calcular el promedio de los dígitos mediante una función.
# - Determinar la posición del dígito mayor dentro del número.
# - Contar la cantidad de dígitos primos en el número mediante una función.
# - Ordenar los dígitos de menor a mayor utilizando Selección Sort y mostrar el resultado.

# Búsqueda de un dígito ingresado por teclado:
# - Pedir al usuario que ingrese un dígito.
# - Informar si se encuentra entre los dígitos del número.
# - Si no se encuentra, solicitar otro ingreso hasta que se ingrese un dígito presente en el número.
# - Usar búsqueda binaria para la verificación.

def num_to_list(num, numList):
    while num != 0:
        d = num % 10
        num = num // 10
        numList.append(d)
    print(f'DNI invertido: {numList}')

def promedio(numList):
    suma = 0
    for i in range(len(numList)):
        suma += numList[i]
    return suma / len(numList)

def seleccion_sort(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

def mayor(lista):
    max = 0
    maxIndex = 0
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
            maxIndex = i
    return max, maxIndex

def es_natural(n):
    return n > 0 and n % 1 == 0

def es_primo(num):
    if num <= 2:
        return False
    elif not es_natural(num):
        return False
    else:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i+=1
        return True

def busq_binaria(lista, dato):
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

def cant_primos(lista):
    primos = 0
    for i in range(len(lista)):
        if es_primo(lista[i]):
            primos += 1
    return primos

def main():
    dniList = []
    dni = int(input("Ingrese su dni: ")) # al ser int Python ignora los ceros a la izquierda
    while dni < 4000000 or dni > 50000000:
        dni = int(input("Ingrese un dni valido: "))
    num_to_list(dni, dniList)

    avg = promedio(dniList)
    print(f'El promedio es {avg}')

    numMax, mayorIndice = mayor(dniList)
    print(f'El numero mayor es {numMax} en el indice {mayorIndice}')

    prim = cant_primos(dniList)
    print(f'Hay {prim} digitos primos')

    seleccion_sort(dniList)
    print(f'DNI ordenado: {dniList}')

    N = int(input("Ingrese digito a buscar: "))
    while N < 0 or N > 10:
        N = int(input("Ingrese un digito valido (1-10): "))

    index = busq_binaria(dniList, N)
    while index == -1:
        N = int(input("Digito no encontrado, ingrese otro (1-10): "))
        while N < 0 or N > 9:
            N = int(input("Ingrese un digito valido (1-10): "))

    print(f'Digito {N} encontrado en posicion {index}')

if __name__ == "__main__":
    main()
