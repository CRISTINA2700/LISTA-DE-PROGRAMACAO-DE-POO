notas = []

for i in range(5):
    nota = float(input("Nota: "))
    notas.append(nota)

print("Notas:", notas)
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
print("Média:", sum(notas) / len(notas))