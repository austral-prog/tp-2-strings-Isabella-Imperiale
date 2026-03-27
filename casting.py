def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = int(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el descuento: "))
    precio_descuento = precio - descuento
    cantidad = int(input("Ingrese la cantidad: "))
    total = precio_descuento * cantidad

    print("Precio: " + str(precio))
    print("Descuento: " + str(descuento))
    print("Precio con descuento: " + str(precio_descuento))
    print("Total: " + str(total))

#casting()