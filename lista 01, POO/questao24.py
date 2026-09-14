soma = 0
cont = 0

for i in range(5):
    valor = float(input("Valor: "))
    if 0 < valor < 1000:
        soma += valor
        cont += 1

if cont > 0:
    print("Média:", soma / cont)
else:
    print("Nenhum valor válido.")