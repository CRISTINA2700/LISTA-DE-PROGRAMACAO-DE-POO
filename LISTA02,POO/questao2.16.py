alunos = {
    "Ana": 8.5,
    "Carlos": 6.5,
    "Maria": 9.0
}

for nome, nota in alunos.items():
    print(nome)
    print("Nota:", nota)

    if nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")