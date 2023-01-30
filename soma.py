soma = 0.0 

dado = input("Digite um número ou aperte 'Enter' para encerrar: ")
while dado != "": 
    numero = float(dado)
    soma += numero
    dado = input("Digite um número ou aperte 'Enter' para encerrar: ")
if dado == "":
    print(soma)