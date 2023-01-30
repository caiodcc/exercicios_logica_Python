import random

menor = int(input("Digite o menor número: "))
maior = int(input("Digite o maior número: "))

numero_secreto = random.randint(menor, maior)
contador = 0

while True:
    contador += 1
    chute = int(input("Digite seu chute: "))
    if chute < numero_secreto:
        print("Número muito baixo!")
    elif chute > numero_secreto:
        print("Número muito alto!")
    else:
        print("Parabéns, você acertou em ", contador, "tentativas")
        break