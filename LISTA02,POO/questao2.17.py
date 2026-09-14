agenda = {
    "Ana": "99999-1111",
    "João": "98888-2222",
    "Maria": "97777-3333"
}

nome = input("Nome: ")

if nome in agenda:
    print("Telefone:", agenda[nome])
else:
    print("Contato não encontrado.")