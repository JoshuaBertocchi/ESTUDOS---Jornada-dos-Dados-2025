
try:
    palavra = input(str("Me informe a palavra: "))

    tranformar_lista = list(palavra)
    lista_invertida = list(palavra[::-1])
    
    if  tranformar_lista == lista_invertida: 
        print(tranformar_lista, lista_invertida)
    else:
        print('error')

     
except ValueError as error:
    print(f"Error : {error}")