import math

area = float(input("Defina a área: "))
if area > 0:
    raio = math.sqrt(area / math.pi)
    print("A área do raio é: ", raio)
else: 
    print("Erro: a área deve ser um número positivo.")
