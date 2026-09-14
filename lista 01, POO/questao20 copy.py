nome = input("Nome: ")
idade = int(input("Idade: "))

if idade >= 18:
    print(nome, "pode entrar desacompanhado.")
else:
    print(nome, "deve entrar acompanhado por um responsável.")