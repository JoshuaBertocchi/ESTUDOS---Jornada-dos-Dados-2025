#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

print(" Vamos calcular o resto da divisão! ")

valor_01 = int(input("Valor 01: "))
valor_02 = int(input("Valor 02: "))

divisao = valor_01 / valor_02
resto_divisao = valor_01 % valor_02

if resto_divisao > 0: 
    print(f"O resultado da divisão é: {divisao} e o resto {resto_divisao}")

else: 
    print(f"O resultado da divisão é: {divisao}")