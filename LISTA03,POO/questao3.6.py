a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

inicio = min(a, b)
fim = max(a, b)

for i in range(inicio, fim + 1):
    print(i)
