arquivo = open("pessoas.csv")
dados = arquivo.read()
arquivo.close
# .splitline é usado para dividir as linhas
for registro in dados.splitlines():
    print("Nome: {}, Idade: {}".format(*registro.split(",")))
