a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não há raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print("Raiz:", x)
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Raiz 1:", x1)
    print("Raiz 2:", x2)