#!/urs/local/bin/python3
from math import pi
import area_circuferencia_v8

def circulo(raio):
    print("àrea do círculo", pi * float(raio) ** 2)

if __name__ == "__main__":
    raio = input("Informe seu raio:")
    circulo(raio)    


