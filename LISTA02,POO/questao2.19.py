equipamentos = {
    "Notebook": {
        "Marca": "Dell",
        "Situação": "Funcionando"
    },
    "Impressora": {
        "Marca": "HP",
        "Situação": "Manutenção"
    }
}

for equipamento, dados in equipamentos.items():
    print(equipamento)
    for chave, valor in dados.items():
        print(chave, ":", valor)

boletim = {
    "João": {
        "Nota1": 8.0,
        "Nota2": 7.5
    }
}

for aluno, notas in boletim.items():
    media = (notas["Nota1"] + notas["Nota2"]) / 2

    print("Aluno:", aluno)
    print("Nota 1:", notas["Nota1"])
    print("Nota 2:", notas["Nota2"])
    print("Média:", media)

    if media >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")