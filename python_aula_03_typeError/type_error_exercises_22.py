

palavra = input("Me informe a palavra: ")
if isinstance (palavra,str):
    tranformar_lista = list(palavra.upper()) #Transforma a palavra em Lista
    #lista_invertida = list(palavra[::-1]).upper() #Cria uma lista invertida
    lista_invertida = list(reversed(palavra.upper())) #Cria uma lista invertida

    if  tranformar_lista == lista_invertida: 
        print(tranformar_lista, lista_invertida)
        print(f"A palavra é polimorfica: {palavra}")
    else:
        print('A palavra não se classifica como Polimórfica')
else: 
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
    