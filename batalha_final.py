#A Batalha Final
#a. Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
#espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
#escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
#70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
#determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
#busque uma nova arma.
#b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.
from random import randint

espada_ataq = randint(30, 120)
espada_dur =  randint(40, 80)


arco_ataq = randint(20, 90)
arco_dur =  randint(80, 150)


lanca_ataq = randint(70, 100)
lanca_dur =  randint(30, 120)

if espada_ataq > 50 and espada_dur>70:
    print(f"O ataque da espada é de {espada_ataq} e a durabilidade da espada é de {espada_dur}.")
    print("A espada é uma boa arma.")
elif arco_ataq >50 and arco_dur > 70:
    print(f"O ataque do arco é de {lanca_ataq} e a durabilidade do arco é de {arco_dur}.")
    print("O arco é uma boa arma.")
elif lanca_ataq >50 and lanca_dur > 70:
    print(f"O ataque da lança é de {lanca_ataq} e a durabilidade da laça é de {lanca_dur}.")
    print("A lança é uma boa arma.")
else:
    print("Escolha outra arma.")



