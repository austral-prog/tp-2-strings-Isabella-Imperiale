def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"

    longitud = len(palabra)

    print("Palabra: " + str(palabra))
    print("Longitud: " + str(longitud))
    print("Primera letra: " + str(palabra[0]))
    print("Ultima letra: " + str(palabra[-1]))
    print("Repetida: " + str(palabra * 3))
    print("Decorada: " + str("*"*3 + palabra + "*"*3))


string_info()