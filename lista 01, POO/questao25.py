horas = int(input("Horas de estudo: "))

if horas < 10:
    print("Quantidade muito baixa.")
elif horas > 40:
    print("Quantidade muito alta.")
else:
    print("Plano configurado com", horas, "horas.")