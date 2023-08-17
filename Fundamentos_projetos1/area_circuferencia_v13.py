#!/urs/local/bin/python3
from math import pi
import sys
import errno

def help(script):
    print("è necessário informar o raio do circulo.")
    print("Sintaxe: é {} <area> <raio>".format(script))

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        # sys.exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print("Àrea do circulo", area)
