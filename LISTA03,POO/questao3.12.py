soma = 0
contador = 0

while contador < 10:
    n = int(input("Digite um número divisível por 3: "))

    if n % 3 == 0:
        soma += n
        contador += 1
    else:
        print("Número inválido!")

print("Soma:", soma)