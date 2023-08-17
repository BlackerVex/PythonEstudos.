PALAVRAS_PROIBIDAS = ("futebol", "religião", "política")
textos = [
    "joão gosta de futebol e política",
    "A praia foi divertida"
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("O texto possui pelo menos uma palavra proíbida:", palavra)
            break
    else:
        print("texto Autorizado:", texto)
        