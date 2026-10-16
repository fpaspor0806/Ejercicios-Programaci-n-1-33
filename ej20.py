def main():

    telefono = input("Introduce el teléfono (+34-número-extensión): ")

    numero = telefono.split("-")[1]
    print(numero)



if __name__ == "__main__":
    main()