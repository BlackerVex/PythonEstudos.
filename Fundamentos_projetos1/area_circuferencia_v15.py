#!/urs/local/bin/python3
from math import pi
import sys
import errno

ERRO = "\033[91m"
NORMAL = "\033[0m"



def help(script):
    print(ERRO,"è necessário informar o raio do circulo.",NORMAL)
    print("Sintaxe: é {} <area> <raio>".format(script))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1]:
        help(0)
        print("O raio deve ser um valor numérico")
        sys.exit(errno.EINVAL)

        raio = sys.argv[1]
        area = circulo(raio)
        print("Àrea do circulo", area)
