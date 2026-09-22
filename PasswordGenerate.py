import random


numeros = "0123456789"
letras = "abcdefghijklmnñopqrstuvwxyz"
simbolos = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~,'


def generar_contraseña():
    longitud = int(input("Escribe un numero maximo de caracteres para tu contraseña: "))
    todos_los_caracteres = numeros + letras + simbolos
    contraseña = random.choices(todos_los_caracteres, k=longitud)
    contraseña_lista = "".join(contraseña)
    print(contraseña_lista)

generar_contraseña()

















