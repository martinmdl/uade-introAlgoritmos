##############################################################
# Se basa en comparar cada elemento con el que tiene a su derecha.
# Si es necesario, se los intercambia
def ordenamiento_intercambio(lista):
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

# Ordena de mayor a menor y funciona con matrices
def ordenamiento_intercambio_desc(matriz):
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

##############################################################
# Comienza a ordenar a partir del segundo elemento de la lista.
# Consiste en mover cada elemento del arreglo hacia la izquierda, haciendolo retroceder hasta encontrar su ubicacion definitiva.
def ordenamiento_insercion(lista):
	for i in range(1, len(lista)):
		aux = lista[i]
		j = i
		while j>0 and lista[j-1]>aux:
			lista[j] = lista[j-1]
			j = j - 1
		lista[j] = aux	
          
##############################################################
# El ordenamiento por selección funciona buscando el mínimo en el resto de la lista y luego hace un solo intercambio por iteración externa.
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]