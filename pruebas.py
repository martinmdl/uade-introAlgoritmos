def metododeintercambio(lista):
    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenada = True

lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,3,5,6,7,4]
lista3 = [2,8,6,1,4,3,7]

print(lista1)
print(lista2)
print(lista3)

metododeintercambio(lista1)
metododeintercambio(lista2)
metododeintercambio(lista3)

print(lista1)
print(lista2)
print(lista3)