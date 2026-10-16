def main():
    Correo = str(input("Introduce tu correo electronico:"))
    Nombre = Correo.split("@")[0]

    print(Nombre + "@ceu.es")

if __name__ == "__main__":
    main()