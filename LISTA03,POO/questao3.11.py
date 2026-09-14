maior = float(input("Digite o 1º valor: "))
for i in range(14):
    valor = float(input("Digite outro valor: "))
    if valor > maior:
        maior = valor

print("Maior valor:", maior)