aprovados = 0

for i in range(4):
    nota = float(input("Nota do aluno: "))

    if nota >= 7:
        aprovados += 1

print("Quantidade de aprovados:", aprovados)