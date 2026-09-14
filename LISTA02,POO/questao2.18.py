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