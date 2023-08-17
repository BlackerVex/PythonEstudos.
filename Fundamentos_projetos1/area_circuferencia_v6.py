#!/urs/local/bin/python3
import time
from math import pi
import area_circuferencia_v6

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

print("Nome do módulo", __name__)
print("Nome do pacóte", __package__)

