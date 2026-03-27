def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura
    perimetro = (base*2) + (altura*2)

    print("Base: " + str(base))
    print("Altura: " + str(altura))
    print("Area: " + str(area))
    print("Perimetro: " + str(perimetro))

#rectangle()