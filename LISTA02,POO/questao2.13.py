disciplina = {
    "nome": "Programação",
    "professor": "Lucas",
    "carga_horaria": 60,
    "periodo": "2026.1"
}

chave = input("Digite a chave: ")

if chave in disciplina:
    print("A chave existe.")
else:
    print("A chave não foi encontrada.")