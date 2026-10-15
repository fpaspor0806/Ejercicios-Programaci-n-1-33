def main():
    Num1 = int(input("Introduce un numero entero"))
    Num2 = int(input("Introduce otro numero entero"))
    coc = Num1 // Num2
    res = Num1 % Num2
    print(f"la división de {Num1} entre {Num2} da un cociente {coc} y un resto {res}")
if __name__ == "__main__":
    main()