while True:
    temp = float(input("Temperatura: "))

    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")

    op = int(input("Escolha: "))

    if op == 1:
        print((temp * 9/5) + 32)
    elif op == 2:
        print((temp - 32) * 5/9)
    elif op == 3:
        print(temp + 273.15)
    elif op == 4:
        print(temp - 273.15)

    resp = input("Deseja continuar? (s/n): ")

    if resp.lower() != "s":
        break