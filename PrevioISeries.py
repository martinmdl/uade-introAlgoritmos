import random

def numerosRandom(lista):
    for i in range(110):
        num = random.randint(100,300)
        if num not in lista:
            lista.append(num)
        
def numeroUnico(lista, dato):
    for numero in lista:
        if numero == dato:
            return False
    return True

def numeroValido(numero):
    if  numero >=100 and numero <=300:
        return True

def metodoBurbujero(lista):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                desordenado = True
    return lista

def burbujeroDescMatriz(matriz):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(matriz) - 1):
            if matriz[i][1] < matriz[i+1][1]:
                aux = matriz[i+1]
                matriz[i+1] = matriz[i]
                matriz[i] = aux
                desordenado = True
    return matriz


def main ():
    ISeries = []
    votos = []

    contador=0
    
    numerosRandom(ISeries)
    metodoBurbujero(ISeries)
    
    for i in range(len(ISeries)):
        fila = []
        fila.append(ISeries[i])
        fila.append(0)
        votos.append(fila)

    for i in range(0, len(ISeries), 10):
        print(*ISeries[i:i+10], sep=", ")

    n= int(input('Ingresar un codigo que pertenezca a una serie valida: '))
    
    while n!=99:
        fila = []
        while not(numeroValido(n)):
            print('ERROR, SERIE INEXISTENTE\n')
            n=int (input('Ingresa una serie existente entre (100-300): '))
        
        if numeroUnico(ISeries,n):
            print(f'El numero {n} no esta en la lista')
        else:
            print(f'El numero {n} esta en la lista')

        for voto in votos:
            if n == voto[0]:
                voto[1] += 1
        
        n= int(input('Ingresar un codigo que pertenezca a una serie valida: '))

    votos = burbujeroDescMatriz(votos)
    print(f'CODIGO\t\t| VOTOS')
    for fila in votos:
        print(f"{fila[0]}\t\t| {fila[1]}")



if __name__ == "__main__":
    main()
    
