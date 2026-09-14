n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha: "))

if op == 1:
    print(n1 + n2)
elif op == 2:
    print(n1 - n2)
elif op == 3:
    print(n1 * n2)
elif op == 4:
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Divisão por zero!")
else:
    print("Opção inválida.")