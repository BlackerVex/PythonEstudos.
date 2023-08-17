#!/usr/local/bin/python3

def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: ter a condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

if __name__ == "__main__":
    # listar os 20 primeiros números da sequência
    for fib in fibonacci(20, (4, 5)):
        print(fib)
