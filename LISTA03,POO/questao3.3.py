menor_igual = 0
maior = 0
soma = 0
maior_latencia = 0

for i in range(10):
    latencia = float(input(f"Teste {i+1}: "))

    soma += latencia

    if latencia <= 100:
        menor_igual += 1
    else:
        maior += 1

    if latencia > maior_latencia:
        maior_latencia = latencia

media = soma / 10

print("Testes <= 100 ms:", menor_igual)
print("Testes > 100 ms:", maior)
print("Média:", media)
print("Maior latência:", maior_latencia)