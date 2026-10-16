def main():
    num = int(input("Introduce un número: "))

    if num < 2:
     print(f"{num} no es primo")
    else:
        es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    print(f"{num} es primo" if es_primo else f"{num} no es primo")

if __name__ == "__main__":
    main()