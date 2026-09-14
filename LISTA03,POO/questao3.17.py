vogais = 0
consoantes = 0

for i in range(10):
    letra = input("Digite uma letra: ").lower()

    if letra in "aeiou":
        vogais += 1
    else:
        consoantes += 1

print("Vogais:", vogais)
print("Consoantes:", consoantes)