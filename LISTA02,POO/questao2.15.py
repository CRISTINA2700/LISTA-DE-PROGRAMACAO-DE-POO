disciplina = {
    "Nome": input("Nome da disciplina: "),
    "Professor": input("Professor: "),
    "Carga Horária": int(input("Carga horária: ")),
    "Quantidade de alunos": int(input("Quantidade de alunos: ")),
    "Situação": input("Situação: ")
}

for chave, valor in disciplina.items():
    print(chave, ":", valor)