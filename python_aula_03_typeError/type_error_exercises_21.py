
print("Converta a temperatura de Celsius para Fahrenheit")

while True:
    try: 
        valor_usuario = float(input("Infome o valor: ")) 
        if isinstance(valor_usuario, (int, float)):
            conversor_c_para_fahrenheit = (valor_usuario * 1.8) +  32
            print(f"Valor Convertido:{conversor_c_para_fahrenheit}°f")    
        break
    except ValueError as e :
        print(f"\033[1;31mErro! Informe apenas números.\n{e}\033[0m") #colori o print




