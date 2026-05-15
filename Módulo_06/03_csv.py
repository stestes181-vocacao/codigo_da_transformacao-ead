import csv

arquivo = open("notas.csv", "w", newline="")

escrever = csv.writer(arquivo)
escrever.writerow(["Nome", "Nota"])
escrever.writerow(["fanny", 10])

arquivo.close()

arquivo = open("notas.csv", "r")

ler = csv.reader(arquivo)
for linha in ler:
    print(linha)

arquivo.close()