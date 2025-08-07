# Cálculo de Envíos y Facturación en un Restaurante
# Un restaurante con servicio de delivery cobra sus envíos según la distancia de entrega:
#
# Tarifas:
# * De 1 a 20 cuadras: $500 fijo.
# * De 21 a 50 cuadras: $70 por cuadra adicional.
# * Desde la cuadra 51 en adelante: $100 por cuadra adicional.
# * Compras mayores a $15,000: Envío gratis.
#
# Ejemplos:
# - Cliente a 8 cuadras → Paga $500 de envío.
# - Cliente a 42 cuadras → Paga $500 + ($70 × 22) = $2040.
# - Cliente a 56 cuadras → Paga $500 + ($70 × 30) + ($100 × 6) = $3200.
#
# Requisitos del programa:
# 1) Generar datos aleatorios para los clientes:
# * DNI: Entre 5,000,000 y 40,000,000.
# * Importe de la compra: Entre $3,000 y $30,000.
# * Cantidad de cuadras: Entre 1 y 100.
#
# 2) Imprimir un listado con:
# * DNI del cliente.
# * Distancia recorrida.
# * Precio total abonado (compra + envío).
#
# 3) Ordenar el listado de mayor a menor por precio total abonado.
#
# Consideraciones:
# * La cantidad de clientes se ingresa por teclado.
# * Los clientes pueden repetirse, pero cada compra se cobra por separado.

import random

# def exists(lista, dato):
#     for i in range(len(lista)):
#         if lista[i] == dato:
#             return True
#     return False

def cargar_datos(m, N):
    for i in range(N):
        dni = random.randint(5000000, 40000000)
        cuadras = random.randint(1, 100)
        importe = random.randint(3000, 30000)
        envio = calcular_envio(cuadras, importe)

        # innecesario porque clientes pueden repetirse
        # while exists(m[0], dni):
        #     dni = random.randint(5000000, 40000000)

        m[0].append(dni)
        m[1].append(cuadras)
        m[2].append(importe)
        m[3].append(importe + envio)



def calcular_envio(cuadras, importe):
    if importe > 15000:
        return 0

    if cuadras <= 20:
        return 500
    elif cuadras <= 50:
        return 500 + 70 * (cuadras - 20)
    else:
        return 500 + 70 * 30 + 100 * (cuadras - 50)


def imprimir(m):
    print("DNI\t\t\tCUADRAS\t\tIMPORTE\t\tTOTAL")
    for i in range(len(m[0])):
        dni = m[0][i]
        cuadras = m[1][i]
        importe = m[2][i]
        total = m[3][i]
        print(f'{dni}\t{cuadras}\t\t\t{importe}\t\t{total}')

def ordena_matriz_burbuja(m):
    # el total esyta en m[3]
    largo = len(m[0])
    for i in range(largo - 1):
        for j in range(largo - i - 1):
            if m[3][j] < m[3][j + 1]:
                m[0][j], m[0][j + 1] = m[0][j + 1], m[0][j]
                m[1][j], m[1][j + 1] = m[1][j + 1], m[1][j]
                m[2][j], m[2][j + 1] = m[2][j + 1], m[2][j]
                m[3][j], m[3][j + 1] = m[3][j + 1], m[3][j]

def main():
    matriz = [[], [], [], []]

    cant = int(input("Ingrese cantidad de clientes: "))
    while cant < 0:
        cant = int(input("Cantidad debe ser positiva.\nIngrese cantidad de clientes: "))

    cargar_datos(matriz, cant)

    ordena_matriz_burbuja(matriz)
    imprimir(matriz)



if __name__ == "__main__":
    main()