nome = input("Nome: ")

disciplinas = []
for i in range(4):
    disciplinas.append(input(f"Disciplina {i+1}: "))

ano_ingresso = int(input("Ano de ingresso: "))
ano_atual = int(input("Ano atual: "))

print("Nome:", nome)
print("Disciplinas:", disciplinas)
print("Tempo de graduação:", ano_atual - ano_ingresso, "anos")