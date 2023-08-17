#!/urs/local/bin/python3
from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == "__main__":
    print(sys.argv[0])
    raio = input("Informe seu raio:")
    area = circulo(raio)    
    print("Àrea do circulo", area)

   


