def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre = input("Ingrese su nombre: ")
    posicion_a = "a" in nombre.lower()
    posicion_e = "e" in nombre.lower()
    posicion_i = "i" in nombre.lower()
    posicion_o = "o" in nombre.lower()
    posicion_u = "u" in nombre.lower()

    print("Contiene a: " + str(posicion_a))
    print("Contiene e: " + str(posicion_e))
    print("Contiene i: " + str(posicion_i))
    print("Contiene o: " + str(posicion_o))
    print("Contiene u: " + str(posicion_u))

#check_vowels()