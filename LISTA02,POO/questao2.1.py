soma = 0

for i in range(6):
    numero = int(input("Digite um número par: "))
    while numero % 2 != 0:
        numero = int(input("Número inválido. Digite um número par: "))
    soma += numero

print("Soma =", soma)