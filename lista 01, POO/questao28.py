x = float(input("X: "))
y = float(input("Y: "))

if x > 0 and y > 0:
    print("Primeiro Quadrante")
elif x < 0 and y > 0:
    print("Segundo Quadrante")
elif x < 0 and y < 0:
    print("Terceiro Quadrante")
elif x > 0 and y < 0:
    print("Quarto Quadrante")
else:
    print("O ponto está sobre um eixo ou na origem.")