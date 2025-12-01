
#%%
# Solicita ao usuário que digite seu nome
nome_valido:bool = False
salario_valido:bool = False
bonus_valido = False
while not nome_valido:
    try:
        nome:str = input("Digite seu nome: ")
        #Verifica se o nome está vazio
        if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio!")
        #Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
                raise ValueError ("Nome não pode conter números!")
        else: 
            print("Nome válido", nome)
            exit()
    except ValueError as e:
          print("Algo está errado", e)
          

# %%
