""" Escribir una función que pida un número entero entre 1 y 10 
y guarde en un fichero con el nombre tabla-n.txt 
la tabla de multiplicar de ese número, done n es el número introducido. """

def save_file(file_name, number):
    with open(file_name, 'w') as file:
        for i in range(11):
            file.write(f"{number} * {i} = {number *i} \n" )

def main():
    number = int(input("Ingrese un numero: "))
    file_name = "tabla-"+str(number)+".txt"
    save_file(file_name, number)

if __name__ == "__main__":
    main()