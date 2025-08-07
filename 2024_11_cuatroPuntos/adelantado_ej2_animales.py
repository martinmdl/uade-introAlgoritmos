# Ejercicio 2 (2 puntos + 0,5 por uso de funciones con parámetros + 0,5 por implementación de ordenamiento por selección)
#  Filtrar y Ordenar Animales por Longitud del Nombre: Crear una lista de al menos 15 nombres de animales.
# El programa debe:
# Seleccionar los nombres que tengan más de 8 caracteres. // Hice mayor o igual para que haya
# Guardar estos nombres en una nueva lista.
# Ordenar la nueva lista en orden alfabético utilizando el algoritmo de ordenamiento por selección (Selection Sort).
# Mostrar la nueva lista ordenada.
# Restricciones:
#  ✅ La selección de nombres y el ordenamiento deben implementarse manualmente.
#  ✅ No se permite el uso de métodos predefinidos como sort o sorted.
from itertools import count


def longPalabra(palabra):
    count = 0
    for _ in palabra:
        count += 1
    return count

def longitudLista(lista):
    count = 0
    for _ in range(lista):
        count += 1
    return count

def mas8Char(lista):
    newList = []
    for i in range(longitudLista(lista)):
        if longPalabra(lista[i]) >= 8:
            newList.append(lista[i])
    return newList

def seleccion(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

def main():
    animales = ["Tortuga", "Gato", "Perro", "Elefante", "Loro", "Leopardo", "Tucan", "Tiburon", "Camaleon",
                "Tigre", "Coyote", "Koala", "Panda", "Vaca", "Cerdo"]

    animalesMas8 = mas8Char(animales)

    print(animalesMas8)

    seleccion(animalesMas8)

    print(animalesMas8)

if __name__ == "__main__":
    main()