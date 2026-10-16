def main():

    preciopan = 3.49
    BarrasPanND = int(input("Introduce el numero de barras de pan no frescas vendidas"))
    
    Preciotot = BarrasPanND * (preciopan * 0.6)

    print(f"El precio habitual del pan es de {preciopan} $")
    print("El descuento de las barras de pan no frescas es del 60%")
    print(f"el precio total de las barras no frescas es de {Preciotot:.2f} $")

if __name__ == "__main__":
    main()