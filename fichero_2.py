""" Escribir una función que pida un número entero entre 1 y 10, 
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
done n es el número introducido, y la muestre por pantalla. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello. """

import os

def main():
    name_numero = int(input("Ingrese un numero del 1 al 10: "))
    file_name = "tabla-" + str(name_numero) + ".txt"

    try:
        file = open(file_name, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print(f'lo siento el fichero {file_name} no existe') 
        exit()

if __name__ == "__main__":
    main()