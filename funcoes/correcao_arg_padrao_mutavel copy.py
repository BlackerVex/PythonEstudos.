def fibonnaci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == "__main__":
    inicio = fibonnaci()
    print(inicio, id(inicio))
    print(fibonnaci(inicio))
    restart = fibonnaci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]