'''
CRUD

SALAO DE BELEZA

Projeto desenvolvido por:
Stefani
Michelle
Rafaela
'''
print('\n === Sistema de Salao de Beleza === \n')

print('1.Ver Agenda')
print('2.Fazer agendamento')
print('3.Escolher Serviço')
print('4.Cancelar Agendamento')
print('5.Mapa')
print('6.Suporte')
print('0.Sair')

agenda = []
while True:
    escolha_menu = input("\nEscolha uma opção: ")
    if escolha_menu == '1':

        
        print('\nVer agenda...')
        if len(agenda) == 0:


            print('Nenhum agendamento')
        else:
            for cliente in agenda:
                print(cliente)

    elif escolha_menu == '2':
        nome_cliente = input('Digite o nome do cliente: ')
        telefone_cliente = input('Digite o telefone do cliente: ')

        agenda.append(nome_cliente)

        print('Agendamento realizado')

    elif escolha_menu == '3':
        print('\nServiços disponíveis')
        print('Cabelo')
        print('Unha')
        print('Maquiagem')


    elif escolha_menu == '4':
        nome = input('Digite o nome para cancelar: ')
        if nome in agenda:
            agenda.remove(nome)
            print('Agendamento cancelado')

    elif escolha_menu == '5':
        print('Mapa do salão disponível')


    elif escolha_menu == '6':
        print('Suporte: (11) 90063-2037')


    elif escolha_menu == '0':
        print("Saindo do sistema. Até breve!")
        break


    else:
        print("Opção inválida. Por favor, tente novamente.")