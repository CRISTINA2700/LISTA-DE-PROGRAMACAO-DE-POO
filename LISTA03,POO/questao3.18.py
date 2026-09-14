nomes = []
precos = []

for i in range(5):
    nome = input("Nome: ")
    preco = float(input("Preço: "))

    nomes.append(nome)
    precos.append(preco)

maior = max(precos)
indice = precos.index(maior)

print("Equipamentos:", nomes)
print("Mais caro:", nomes[indice])
print("Preço:", maior)