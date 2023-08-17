def opcao1():
    print("Domingo é Fim de semana")
def opcao2():
    print("Segunda È meio da semana")
def opcao3():
    print("terça È meio da semana")
def opcao4():
    print("Quarta È meio da semana")
def opcao5():
    print("Quinta È meio da semana")
def opcao6():
    print("Sexta È meio da semana")
def opcao7():
    print("Sábado é Fim de semana")

opcoes = {
    1: opcao1,
    2: opcao2,
    3: opcao3,
    4: opcao4,
    5: opcao5,
    6: opcao6,
    7: opcao7,

}
while True:
    print("Escolha uma opção!")
    print("1 = Domingo")
    print("2 = Segunda")
    print("3 = Terça")
    print("4 = Quarta")
    print("5 = Quinta")
    print("6 = Sexta")
    print("7 = Sábado")
    print("0 = sair")

    escolha = int(input())

    if escolha == 0:
        break

    if escolha in opcoes:
        opcoes[escolha]()

    


