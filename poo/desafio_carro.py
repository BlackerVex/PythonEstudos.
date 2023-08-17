class Carro:
    def __init__(self, velocida_maxima):
        self.velocida_maxima = velocida_maxima
        self.velocidade_atual = 0
    
    def acelerar(self, delta):
        if self.velocidade_atual + delta > self.velocida_maxima:
            self.velocidade_atual = self.velocidade_maxima
        else:
            self.velocidade_atual += delta
        return self.velocidade_atual
    
    def frear(self, delta):
        if self.velocidade_atual - delta < 0:
            self.velocidade_atual = 0
        else:
            self.velocidade_atual -= delta
        return self.velocidade_atual



if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        # 178
        print(c1.acelerar(8))

    for _ in range(10):
        # 3
        print(c1.frear(delta=20))