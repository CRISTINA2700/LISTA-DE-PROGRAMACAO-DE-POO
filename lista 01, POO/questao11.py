valor = float(input("Valor do empréstimo: "))
taxa = float(input("Taxa de juros (%): "))
meses = int(input("Quantidade de meses: "))

juros = valor * (taxa / 100) * meses
montante = valor + juros

print("Juros:", juros)
print("Montante:", montante)