
try:
    temperatura = int(input("Me informe a temperatura: "))

    if temperatura < 18:
        print("Temperatura Baixa")
    elif temperatura >=18 and temperatura <=26:
        print("Temperatura Normal")
    elif temperatura >=26:
        print("Temperatura Alta")
    else: 
        print("Algo deu errado!")

except ValueError as e:
    print(f"Algo deu errado!\n{e}")