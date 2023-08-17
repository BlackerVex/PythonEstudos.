
class Data:
    def __init__(self, dia=1, mes=1, ano=1070):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

d1 = Data(5, 12, 2020)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2023
print(d1)

d2 = Data(ano=2029, mes=12)
d2.dia = 9
# d2.mes = 1
# d2.ano = 2022
print(d2)