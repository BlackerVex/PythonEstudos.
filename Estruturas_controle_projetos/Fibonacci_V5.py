#!/usr/local/bin/python3

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == "__main__":
    fib_seq = fibonacci(1000)
    sum_seq = sum(fib_seq)
    print(f"{sum_seq}")

