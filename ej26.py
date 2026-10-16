def main():
    productos = str(input("Introduce la cesta de la compra separada por comas: "))
    for productos in productos.split(","):
        print(productos.strip())

if __name__ == "__main__":
    main()