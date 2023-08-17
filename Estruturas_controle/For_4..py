# for i in range (1, 10 + 1):
#     if i == 6:
#         break
#     print(i)
# else:
#     print("Fim!")


    # Atividade 

# from random import randint

# numero_sorteado = randint(1, 6 + 1)
# for numero_sorteado in range (1, 6 + 1):
#     if numero_sorteado % 2 == 0:
#         print(numero_sorteado)
#         print("Acertou")
#         break
#     else:
#         print(numero_sorteado)
#         print("Não acertou o numero")
#         continue


from random import randint

def sortear_dado():
    return randint(1 , 6)

for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print("Acertou", i)
        break
else:
    print("Não acertou o número.") 