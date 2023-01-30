
sentenca = input("Escreva uma sentença: ")
lista_palavras = sentenca.split()
print("Existem", len(lista_palavras), "palavras nesta sentença!")


soma = 0

for palavra in lista_palavras: 
    soma += len(palavra)