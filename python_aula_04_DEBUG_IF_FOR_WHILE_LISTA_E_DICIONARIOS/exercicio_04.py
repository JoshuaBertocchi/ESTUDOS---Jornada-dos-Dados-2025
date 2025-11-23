
try: 
    name_user = "Joshua"#input("Infome seu nome: ")
    email_user = "joshua@email.com" #input("Informe seu E-mail: ")
    idade_user = 20

    if not  18 <= idade_user <=65: 
        print("Idade fora do intervalo permitido")
    elif "@" not in email_user and ".":
        print("Email invalido")
    
    else:
        print('Dados válidos!')

except ValueError as e:
    print(f"Algo deu errado\n{"-----"*10}\n{e}") 
    