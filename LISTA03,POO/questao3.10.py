menor = float(input("Digite a 1ª latência: "))

for i in range(9):
    valor = float(input("Digite outra latência: "))
    if valor < menor:
        menor = valor

print("Menor latência:", menor)