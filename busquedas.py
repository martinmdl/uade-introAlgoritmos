##############################################################
# Búsqueda Secuencial
# Recorre toda la lista hasta encontrar el dato.
# No necesita que la lista esté ordenada.
def busqueda_secuencial(lista, dato):
    for i in range(len(lista)):  # Recorrer toda la lista
        if lista[i] == dato:  # Si encontramos el dato, devolvemos su índice
            return i
    return -1  # Si no encontramos el dato, devolvemos -1

##############################################################
# Búsqueda Binaria
# Requiere que la lista esté ordenada.
# Divide el problema a la mitad cada vez, haciendo que sea mucho más rápida que la búsqueda secuencial.
def busqueda_binaria(lista, dato):
    izq, der = 0, len(lista) - 1  # Inicializamos los índices
    while izq <= der:
        centro = (izq + der) // 2  # Encontramos el centro
        if lista[centro] == dato:
            return centro  # Encontramos el dato
        elif lista[centro] < dato:
            izq = centro + 1  # El dato está en la mitad derecha
        else:
            der = centro - 1  # El dato está en la mitad izquierda
    return -1  # Si no encontramos el dato, devolvemos -1

##############################################################
# Otra busqueda binaria
def busqueda_binaria(lista, valor_buscado):
  posicion = -1
  izq = 0
  der = len(lista)-1
  while (posicion == -1 and izq <= der):
    medio = (izq + der) // 2
    if (lista[medio] == valor_buscado):
      posicion = medio
    else:
      if (valor_buscado > lista[medio]):
        izq = medio + 1
      else:
        der = medio - 1
  return posicion