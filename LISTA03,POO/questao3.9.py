inicio = int(input("Primeiro número: "))
fim = int(input("Último número: "))

if inicio > fim:
    inicio, fim = fim, inicio

soma = 0
quantidade = 0

for i in range(inicio, fim + 1):
    soma += i
    quantidade += 1

print("Média:", soma / quantidade)