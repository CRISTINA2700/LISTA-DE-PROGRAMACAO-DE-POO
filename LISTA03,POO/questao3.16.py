inicio = int(input("Início: "))
fim = int(input("Fim: "))

if inicio > fim:
    inicio, fim = fim, inicio

contador = 0

for i in range(inicio, fim + 1):
    if i % 7 == 0:
        contador += 1

print("Quantidade:", contador)