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










def main ():
  ISeries = []
  votos= []


  contador=0

  numerosRandom(ISeries)
  metodoBurbujero(ISeries)


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
              for serie in ISeries:
                  if n == serie:
                       fila.append(n)
                       fila.append(1)
                       votos.append(fila)





      n= int(input('Ingresar un codigo que pertenezca a una serie valida: '))

  print(f'Estas son las cantdidad de votos {votos}')



if __name__ == "main":
    main()