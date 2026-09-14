class Pokemon:
    def _init_(self, numero, nome, tipo, nivel, hp):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.hp = hp

pokedex = []

while True:
    print("\n1-Cadastrar")
    print("2-Consultar")
    print("3-Atualizar")
    print("4-Excluir")
    print("5-Listar")
    print("0-Sair")

    op = input("Opção: ")

    if op == "1":
        numero = int(input("Número: "))
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        nivel = int(input("Nível: "))
        hp = int(input("HP: "))
        pokedex.append(Pokemon(numero, nome, tipo, nivel, hp))

    elif op == "2":
        numero = int(input("Número: "))
        for p in pokedex:
            if p.numero == numero:
                print(p.numero, p.nome, p.tipo, p.nivel, p.hp)

    elif op == "3":
        numero = int(input("Número: "))
        for p in pokedex:
            if p.numero == numero:
                p.nome = input("Novo nome: ")
                p.tipo = input("Novo tipo: ")
                p.nivel = int(input("Novo nível: "))
                p.hp = int(input("Novo HP: "))

    elif op == "4":
        numero = int(input("Número: "))
        for p in pokedex:
            if p.numero == numero:
                pokedex.remove(p)
                break

    elif op == "5":
        for p in pokedex:
            print(p.numero, "-", p.nome, "-", p.tipo, "-", p.nivel, "-", p.hp)

    elif op == "0":
        break

    else:
          print("Opção inválida!")