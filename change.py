def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    gasto= float(input("Ingresar el gasto: "))
    dinero_recibido= int(input("Ingrese el dinero recibido: "))

    print("Ingresar gasto:") #67.4
    print(gasto)
    print("Dinero recibido") #200
    print(dinero_recibido)
    print("")
    print("Vuelto")
    print("")
    vuelto = dinero_recibido - gasto #132.6
    pesos = int(vuelto)
    print("Pesos:")
    print(pesos)
    centavos = round((vuelto - pesos) * 100)
    print("Centavos:")
    print(centavos)

change()