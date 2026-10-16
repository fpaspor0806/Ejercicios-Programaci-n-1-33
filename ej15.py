def main():
    Dinero = float(input("Introduce el dinero que deseas ahorrar: "))

    Interes1ºaño = Dinero * (1 + 0.04)
    Interes2ºaño = Interes1oaño * (1 + 0.04)
    Interes3ºaño = Interes2oaño * (1 + 0.04)

    print(f"La cantidad de dinero ahorrado en en el primer año es de {Interes1oaño:.2f}$ en el segundo año es de {Interes2oaño:.2f} $ y el tercer año es de {Interes3oaño:.2f} $")
    
if __name__ == "__main__":
    main()
