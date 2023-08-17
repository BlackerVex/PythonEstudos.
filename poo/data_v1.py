class Data:
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2023
print(d1)

d2 = Data()
d2.dia = 9
d2.mes = 1
d2.ano = 2022
print(d2)
