# import math

# def area_circuferencia(raio):
#    area = math.pi * raio**2
#    return area

# print("Digite seu raio:")
# raio = float(input())
# area = area_circuferencia(raio)
# print("Sua área é: {}".format(area))

class terminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"

pi = 3.14159
print(terminalColor.ERRO +  
      "Digite seu raio:" + 
      terminalColor.NORMAL)
raio = float(input())
print("àrea do circulo", pi * raio ** 2)