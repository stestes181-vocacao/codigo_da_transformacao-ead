#atividade 01
rint("=== Calculadora Basica ===")

#Entrada

A = float(input("Me diga um valor: "))
B = float(input("Me diga outro valor: "))

#Processo

Soma = A + B
Subtracao = A - B
Multiplicacao = A * B

#Saída

print("\n---Resultados---")
print(f"{A} + {B} = {Soma}")
print(f"{A} - {B} = {Subtracao}")
print(f"{A} * {B} = {Multiplicacao}")

#Verificação

if B == 0:
print("Divisão: Não é possível dividir por zero")
else:
Divisao = A / B
print(f"{A} / {B} = {Divisao}")

#atividade 02

print("=== Descobrindo o maior número ===")

primeiro = int(input("Digite um número: "))
segundo = int(input("Digite outro número: "))

if primeiro > segundo:
    print(f"O maior número é {primeiro}")
elif segundo > primeiro:
    print(f"O maior número é {segundo}")
else:
    print("Os dois são iguais")
  
#atividade 03
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

#atividade 04 - extra

print("=== Menu de Cálculo ===")

opcao = ""

while opcao != "0":
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        x = float(input("Digite um número: "))
        y = float(input("Digite outro número: "))
        soma = x + y
        print("Soma =", soma)

    elif opcao == "2":
        x = float(input("Digite um número: "))
        y = float(input("Digite outro número: "))
        sub = x - y
        print("Subtração =", sub)

    elif opcao == "0":
        print("Fim do programa")

    else:
        print("Digite uma opção válida")
