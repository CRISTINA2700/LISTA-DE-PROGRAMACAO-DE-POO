softwares = ["Windows", "Office", "Chrome", "Python", "VS Code"]

print("Lista original:")
print(softwares)

novo = input("Digite o nome do novo software: ")
softwares.append(novo)

softwares.pop(1)

print("Lista atualizada:")
print(softwares)
