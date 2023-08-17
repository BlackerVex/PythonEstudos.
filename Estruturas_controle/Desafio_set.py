PALAVRAS_PROIBIDAS = {"futebol", "religião", "política"}
textos = [
    "joão gosta de futebol e política",
    "A praia foi divertida"
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("O texto possui palavras proíbidas", intersecao)
        break
    else:
        print("Texto Autorizado, nenhuma palavra proíbida.", texto)