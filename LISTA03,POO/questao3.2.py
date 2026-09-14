def calcular(a, b):
    produto = a * b

    if produto <= 1000:
        return produto
    else:
        return a + b

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print("Resultado:", calcular(x, y))