def main():
    Ppayasos = 112
    Pmuñecas = 75
    payasos = int(input("Introduce el numero de payasos vendidos en el ultimo pedido: "))
    Muñecas = int(input("Introduce el numero de muñecas vendidas en el ultimo pedido: "))
    PtPayasos = Ppayasos * payasos
    PtMuñecas = Pmuñecas * Muñecas
    Ptotal = (PtMuñecas + PtPayasos) / 100
    print(f"El  peso total del paquete que sera enviado es de {Ptotal} Kg")
if __name__ == "__main__":
    main()