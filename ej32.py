def main():

    num = int(input("¿Cuantos terminos quieres?"))

    a, b = 0, 1
    for _ in range(num):
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    main()