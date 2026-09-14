valor = float(input("Valor financiado: "))
taxa = float(input("Taxa (%): "))
meses = int(input("Meses: "))

juros = valor * (taxa / 100) * meses
montante = valor + juros

print("Juros:", juros)
print("Montante:", montante)