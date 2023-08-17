def faixa_etária(idade):
   if 0 <= idade < 18:
        return "Menor de idade"
   elif idade in range(18, 65):
        return idade in range(65, 100)
        return "Melhor idade"
   elif idade >= 100:
        return "centenário"
   else:
        return "idade inválida"


if __name__ == "__main__":
    for idade in (17, 35, 0, 87, 133, -2):
       print(f"{idade}: {faixa_etária(idade)}")
