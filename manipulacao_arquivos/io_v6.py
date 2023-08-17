with open("pessoas.csv") as arquivo:
    with open("pessoas.txt", "w") as saida:
        for registro in arquivo:
            pessoas = registro.strip().split(",")
            print("Nome: {}, Idade: {}".format(*pessoas), file=saida)

if arquivo.closed:
    print("O arquivo foi fechado!")

if saida.closed:
    print("Arquivo de saída foi fechado!")