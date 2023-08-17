#!/urs/local/bin/python3
import time
from math import pi

if __name__ == "__main2__" :
    print("Bem vindo a calculadora de área!!")
time.sleep(1)
print("Informe o raio: ")
raio = float(input())
print("Calculando ===========")
time.sleep(3)
resultado = pi * raio ** 2
print("Seu Resultado foi Calculado!")
time.sleep(2)
print("Sua área é: {:.2f}".format(resultado))


