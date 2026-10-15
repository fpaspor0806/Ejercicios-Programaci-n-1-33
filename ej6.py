def main():
    print("Se ha aplicado un iva del 10%")
    Iva = 0.1
    Imp_ci = float(input("introduce el importe del articulo"))
    Imp_SI = Imp_ci - (Imp_ci * Iva)
    print(f"El importe sin iva es de {Imp_SI} $")
if __name__ == "__main__":
    main()