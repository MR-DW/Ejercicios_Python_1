# 3. Escriba un programa que lea 1 palabra (ingresadas por el usuario), calcule la longitud de cada una de ellas y
# las despliegue junto con su longitud indicada con asteriscos. Ejemplo:
# Árbol *****
# Celular *******
# Uno ***

from logging.config import dictConfig


palabra = input("Escriba su palabra: ")
palabra2 = input("Escriba su palabra: ")
palabra3 = input("Escriba su palabra: ")
# cant_asteriscos = len(palabra)
# asteriscos = cant_asteriscos
print(palabra, "\t" + "*"*len(palabra))
print(palabra2, "\t" + "*"*len(palabra2))
print(palabra3, "\t" + "*"*len(palabra3))

diccionario = {
    "palabra":palabra, 
    "palabra2":palabra2,
    "palabra3":palabra3,
              }

print(diccionario)