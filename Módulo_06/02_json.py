import json

clientes = {
    "nome": "Stefani",
    "idade": 17
}
arquivo = open("clientes.json", "w")

json.dump(clientes, arquivo)

arquivo.close()
arquivo = open("clientes.json", "r")

print(json.load(arquivo))

arquivo.close()