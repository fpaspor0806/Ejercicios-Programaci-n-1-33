def main():
    peso = float(input("Introduce tu masa corporal en kg: "))
    altura = float(input("Introduce tu estatura en metros: "))
    Imc = peso / (altura * altura)
    print(f"Tu índice de masa corporal es {Imc:.2f}")
if __name__ == "__main__":
    main()