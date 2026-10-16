def main():

    Usuario = str(input("Introduce tu nombre"))
    Nombre = (Usuario.upper())
    letras = len(Usuario.replace(" " , ""))

    print(f"{Nombre} tiene {letras} letras")

if __name__ == "__main__":
    main()