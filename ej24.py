def main():
    precio = input("Introduce el precio (€): ")

    euros, centimos = precio.split(".")
    print(euros, "euros y", centimos, "céntimos")

if __name__ == "__main__":
    main()