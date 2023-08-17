def imprimir(maximo, atual):
    # Condição de parada
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)


imprimir(100, 1)
