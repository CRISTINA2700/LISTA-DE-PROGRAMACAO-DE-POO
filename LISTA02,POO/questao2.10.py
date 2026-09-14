estudante = {
    "Nome": input("Nome: "),
    "Matrícula": input("Matrícula: "),
    "Idade": int(input("Idade: ")),
    "Curso": input("Curso: "),
    "Semestre": int(input("Semestre: "))
}

for chave, valor in estudante.items():
    print(chave + ":", valor)