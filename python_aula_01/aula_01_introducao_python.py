bonus_anual = 1000

nome_usuario = input("Me infome o seu nome: ")

salario_usuario = float(input("Me informe seu salário: "))

bonus_usuario = float(input("Qual é o valor do bonus? "))


calculo = bonus_usuario + (salario_usuario * bonus_usuario)

print(f"{nome_usuario}, aqui está seu salario: {calculo}")