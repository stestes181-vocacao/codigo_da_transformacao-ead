agenda = {}

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
agenda[nome] = telefone
print("\nAGENDA DE CONTATOS")

for nome, telefone in agenda.items():

    print(nome, "-", telefone)