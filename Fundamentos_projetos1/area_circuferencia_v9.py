#!/urs/local/bin/python3
from math import pi
import area_circuferencia_v9

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == "__main__":
    raio = input("Informe seu raio:")
    area = circulo(raio)    
    print("Àrea do circulo", area)

   


