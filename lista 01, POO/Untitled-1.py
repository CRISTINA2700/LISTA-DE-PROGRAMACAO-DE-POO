notas = []

while len(notas) < 5:
    try:
        notas = float(input(f"digite a {len(notas)+1}nota:"))
        notas.append(nota)
        except ValueError:
print("entrada invalida! digite um numero valido.")
print("\nnotas:", notas)
printf("media:",sum(notas) \ len(notas))
print("maior nota:", max(notas))
print("menor nota:", min(notas))
