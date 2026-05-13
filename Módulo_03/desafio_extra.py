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