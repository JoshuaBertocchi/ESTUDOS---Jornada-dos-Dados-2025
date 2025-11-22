 
try:
    print("Digite os Valores ")
    valor_01 = float(input("Valor 01: "))
    valor_02 = float(input("Valor 02: "))
    
    print("Qual será a operação?")
    operacao = input(str("\nSoma: +\nMenos: -\nDivisão: /\nMultiplicação: *\nDigite o símbolo: "))
    
    if operacao == "+":
        soma = valor_01 + valor_02
        print(f"Soma: {soma}")

    elif operacao == "-":
        diminuicao = valor_01 - valor_02
        print(f"Diminuição: {diminuicao}")            
    elif operacao == "/":
        try:
            divisao = valor_01 / valor_02
            print(f"Divisão: {divisao}")
        except ZeroDivisionError: 
            print("Não é possível divir por zero!")
    elif operacao == "*":
        Multiplicação = valor_01 * valor_02
        print(f"Divisão: {Multiplicação}")
    else:
        print("Digite apenas o símbolo escolhido!")
except ValueError as Error:
    print("Digite apenas o números!")


