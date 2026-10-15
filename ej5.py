def main():
    Imp_si = float(input("introduce el importe sin iva del articulo: "))
    Iva = float(input("Introduce el iva a aplicar: "))
    Imp_ci = Imp_si + (Imp_si * Iva / 100)
    print("el importe con iva es de" ,Imp_ci, "$")
if __name__ == "__main__":
    main()