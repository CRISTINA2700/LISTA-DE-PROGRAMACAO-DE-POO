 quantidade = int(input("Quantidade de notas: "))

    soma = 0

    for i in range(quantidade):
        nota = float(input("Nota: "))
        soma += nota

    media = soma / quantidade
    print("Média =", media)

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except ValueError:
    print("Digite apenas números.")