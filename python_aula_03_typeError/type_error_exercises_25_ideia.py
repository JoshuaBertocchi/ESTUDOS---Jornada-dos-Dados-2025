
print("Me informe vários números!")
lista_valores = []
while True: 
    valor = str(input("Valor: "))
    lista_valores.append(valor) #adiciona na lista
    v = input("Quer continuar? [S/N]").upper()
    if v == "N":
        print(lista_valores)
        break
    elif v == "S":
        print("Certo, vamos continuar")
    else:
        print("Renponda corretamente!")

    

