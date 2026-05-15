def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    print("Média:", media)

    if media >= 7:

        print("Aprovado")

    else:

        print("Reprovado")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

calcular_media(nota1, nota2)