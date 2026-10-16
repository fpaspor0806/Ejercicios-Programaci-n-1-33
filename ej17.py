def main():
    Nombre = str(input("Introduce un nombre: "))
    Lineas = int(input("Introduce un numero de lineas: "))

    for _ in range(Lineas):
        print(f"{Nombre}")

if __name__ == "__main__":
    main()