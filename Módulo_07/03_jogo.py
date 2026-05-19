import random

numero = random.randint(1, 30)

palpite = int(input("Digite um número entre 1 e 30: "))

if palpite == numero:
    print("Você acertou!")
else:
    print("Número errado!")
    print("O número sorteado foi:", numero)