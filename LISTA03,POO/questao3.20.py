memoria = []
soma = 0

for i in range(5):
    valor = float(input("Digite a memória utilizada: "))
    memoria.append(valor)
    soma += valor

print("Soma:", soma)