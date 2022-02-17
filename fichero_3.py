from io import open

def main():
    file = open("tabla-5.txt", 'r')
    line = file.readlines()
    
    for item in line:
        print(item)
        # obteniendo solo un valor -> el resultado
        print(item[8:].lstrip())
    

if __name__ == "__main__":
    main()