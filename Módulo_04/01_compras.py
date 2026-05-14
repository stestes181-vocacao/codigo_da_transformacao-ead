def lista_compras():

    lista = []

    while True:

        print("\nLISTA DE COMPRAS")
        print("1 - Adicionar item")
        print("2 - Ver lista")
        print("3 - Remover item")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            item = input("Digite o item: ")
            lista.append(item)

            print("Item adicionado!")

        elif opcao == "2":

            if len(lista) == 0:
                print("Lista vazia")

            else:
                print("\nItens da lista:")

                for item in lista:
                    print("-", item)

        elif opcao == "3":

            item = input("Digite o item que deseja remover: ")

            if item in lista:
                lista.remove(item)
                print("Item removido!")

            else:
                print("Item não encontrado")

        elif opcao == "4":

            print("Saindo...")
            break

        else:
            print("Opção inválida")


lista_compras()