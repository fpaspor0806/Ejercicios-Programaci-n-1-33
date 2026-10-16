import random

def main():
    
    num1 = int(input("Introduce un numero (1-100)"))
    num2 = int(input("Introduce otro numero (1-100)"))

    print(random.randint(num1 , num2))

if __name__ == "__main__":
    main()