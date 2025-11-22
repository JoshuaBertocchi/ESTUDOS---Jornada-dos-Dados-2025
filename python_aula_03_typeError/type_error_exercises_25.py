
entrada_lista = input("Digite uma lista python com números: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        # 01- Tirandos os espaços vázios. 2- Convertendo em Int 3- Adicionando a lista
        numeros_int.append(int(num.strip()))   
        print(f"Lista de inteiros: {numeros_int}")
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
