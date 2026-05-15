arquivo = open("texto.txt", "w")

arquivo.write("Olá mundo")
arquivo.close()

arquivo = open("texto.txt", "r")

print(arquivo.read())
arquivo.close()