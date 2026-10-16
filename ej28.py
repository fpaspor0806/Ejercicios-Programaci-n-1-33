def main():

    a = float(input("Introduce un 1º lado:"))
    b = float(input("Introduce un 2º lado:"))
    c = float(input("Introduce un 3º lado:"))

    SemiP = (a + b + c) / 2

    if a + b > c and a + c > b and b + c > a:
            SemiP = (a + b + c) / 2
            area = (SemiP * (SemiP - a) * (SemiP - b) * (SemiP - c)) ** 0.5

    print(f"El area del triangulo es igual a {area}")

if __name__ == "__main__":
    main()