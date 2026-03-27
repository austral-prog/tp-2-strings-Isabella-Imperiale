def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input("Escriba su nombre completo: ").lstrip().rstrip()
    email = input("Escriba su email: ")
    nota_1 = input("Ingrese la primera nota: ")
    nota_2 = input("Ingrese la segunda nota: ")
    nota_3 = input("Ingrese la tercera nota: ")
    encabezado ="""========================
    FICHA DEL ALUMNO
========================"""

    print(encabezado)
    print("Nombre: " + str(nombre.title()))
    print("Email: " + str(email.lower()))
    print("Caracteres en nombre: " + str(len(nombre)))
    print("Iniciales: " + str(nombre[0].upper()) + str(nombre[nombre.find(" ")+1].upper()))
    print("Usuario: " + str(nombre[nombre.find(" ")+1:].lower()) + "." + str(nombre[0:nombre.find(" ")].lower()))
    print("Email valido: " + str("@" in email))
    print("Dominio: " + str(email.lower()[email.find("@")+1:]))
    print("Nombre para archivo: " + str(nombre.replace(" ", "_").title()))
    print("Cantidad de a: " + str(nombre.lower().count("a")))
    print("Codigo secreto: " + str(nombre[::-1].upper()))
    print("Nota 1: " + str(nota_1))
    print("Nota 2: " + str(nota_2))
    print("Nota 3: " + str(nota_3))
    print("Suma: " + str((int(nota_1) + int(nota_2) + int(nota_3))))
    print("Promedio: " + str((int(nota_1) + int(nota_2) + int(nota_3))/3))
    print("Promedio entero: " + str((int(nota_1) + int(nota_2) + int(nota_3))//3))
    print("=" * 24)

ficha()