print("1 - Hipotenusa")
print("2 - Cateto")

opcao = int(input("Escolha: "))

if opcao == 1:
    c1 = float(input("Cateto 1: "))
    c2 = float(input("Cateto 2: "))
    h = (c1*2 + c22) * 0.5
    print("Hipotenusa:", h)

elif opcao == 2:
    h = float(input("Hipotenusa: "))
    c = float(input("Outro cateto: "))
    cateto = (h*2 - c2) * 0.5
    print("Cateto:", cateto)

else:
    print("Opção inválida.")-