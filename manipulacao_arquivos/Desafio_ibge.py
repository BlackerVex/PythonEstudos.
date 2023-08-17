import csv

with open("desafiobge.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)
    linhas = []

    for i, linha in enumerate(leitor):
        if i == 2 or i == 8:
            linha.append(linhas)

    print(linha)