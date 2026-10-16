def main():

    producto_nombre = (input("Introduce el nombre del producto:"))
    producto_precio = float(input("Introduce el precio del producto:"))
    producto_cantidad = int(input("Introduce la cantidad de productos:"))
    
    total = producto_precio * producto_cantidad

    print(f"{producto_nombre}, {producto_precio:9.2f}$, {producto_cantidad:3d}unidades, {total:011.2f}euros")

if __name__ == "__main__":
    main()