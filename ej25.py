def main():
    fecha = (input("Introduce tu fecha de nacimiento (dd/mm/aaaa):"))
    dia, mes, año = fecha.split("/")

    print("Dia", int(dia),"Mes",int(mes),"Año",año,)
if __name__ == "__main__":
    main()