def edadValida(edad):
    if edad >= 13 and edad <= 50:
        return True
    
def edadRealista(edad):
    if edad > 0 and edad < 120:
        return True
    
def esUnico(lista, dato):

    for aspirante in lista:
        if aspirante[0] == dato:
            return False
        
    return True

def main():


    contadorValidos = 0
    contadorRechazados = 0
    listaAspirantes = []

    nroSocio = int(input("Ingresar nro socio: "))

    while nroSocio != -1:

        aspirante = []

        while not(nroSocio >= 1000 and nroSocio <= 9999 and esUnico(listaAspirantes, nroSocio)):
            nroSocio = int(input("Error: 4 dígitos y que no se repita: "))


        aspirante.append(nroSocio)

        edadAspirante = int(input("Ingrese edad: "))
        while not(edadRealista(edadAspirante)):
            edadAspirante = int(input("Ingrese edad entre 0 y 120: "))

        if edadValida(edadAspirante):
            contadorValidos += 1
        else:
            contadorRechazados += 1
        
        aspirante.append(edadAspirante)
        listaAspirantes.append(aspirante)

        nroSocio = int(input("Ingresar nro socio: "))

    print(f"Aspirantes válidos: {contadorValidos}")
    print(f"Aspirantes rechazados: {contadorRechazados}")

    print(f"Nro Socio Aspirantes rechazados:")
    
    for aspirante in listaAspirantes:
        if not edadValida(aspirante[1]):
            print(f"# {aspirante[0]}")

    print("\nTOTAL ASPIRANTES")
    print("Nro Socio \t| Edad")

    for aspirante in listaAspirantes:
        print(f"{aspirante[0]} \t\t| {aspirante[1]}")


if __name__ == "__main__":
    main()






























