lista = []

while True:
    print("\nLISTA DE COMPRAS")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Ver lista")
    print("4 - Sair")

    opcao = input("Escolha: ")
    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)
        print("Item adicionado")

    elif opcao == "2":
        item = input("Digite o item para remover: ")

        if item in lista:

            lista.remove(item)
            print("Item removido")

        else:
            print("Item não encontrado")

    elif opcao == "3":
        print("\nLista atual:")

        for item in lista:
            print("-", item)

    elif opcao == "4":
        print("Programa encerrado")
        break