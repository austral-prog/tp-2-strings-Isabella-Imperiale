from encodings.punycode import adapt
from wsgiref.util import application_uri


def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    nom_ape = nombre + " " + apellido

    print(nom_ape.lower())
    print(nombre.capitalize() + " " + apellido.capitalize())
    print(nom_ape.upper())
    print("\t" + nom_ape.lower())

#2names()