from random import randint
print("Jogo da adivinhação!")
computador = randint(1, 100)
while True:
    usuario = int(input("Insira um número de 1 a 100 (ou 0 para sair): "))
    if usuario == 0:
        print("Você saiu do jogo.")
        break
    if usuario < 1 or usuario > 100:
        print("Por favor, insira um número entre 1 e 100.")
        continue

    if usuario == computador:
        print(f"O número escolhido pelo computador foi {computador}, você acertou!")
        break
    elif usuario < computador:
        print("Você errou, o número escolhido pelo computador foi maior que o seu, tente novamente.")
    else:
        print("Você errou, o número escolhido pelo computador é menor que o seu, tente novamente.")

