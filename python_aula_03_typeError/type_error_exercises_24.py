try:
    valor = int(input("Digite um valor: "))
    if isinstance(valor,int):
        if valor <= -1:
            print(f"Valor é Negativo")
        elif valor >= 1:
            print(f"Valor Positivo")
        else:  
            print("Apenas ZERO!")
        
except ValueError as e:
    print(f"Digite apenas número\nErro: {e}".upper())