print("=== Verificação de idade ===")

idade = int(input("Quantos anos você tem? "))

if idade >= 60:
    print("Idoso")

elif idade >= 18:
    print("Adulto")

elif idade >= 13:
    print("Adolescente")

else:
    print("Criança")