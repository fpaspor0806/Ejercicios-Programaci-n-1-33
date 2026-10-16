def main():
    frase = str(input("Introduce una frase:"))
    vocal = str(input("Introduce una vocal:"))

    print(frase.replace(vocal.lower(), vocal.upper()))
if __name__ == "__main__":
    main()