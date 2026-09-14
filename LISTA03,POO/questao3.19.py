valores = []

for i in range(7):
    valores.append(int(input("Digite um valor: ")))

print("Ordem inversa:")

for i in range(6, -1, -1):
    print(valores[i])