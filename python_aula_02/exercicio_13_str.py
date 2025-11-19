data = input("Digite uma data no formato dd/mm/aaaa: ")

# Divide a string usando a barra como separador
dia, mes, ano = data.split("/")

print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)