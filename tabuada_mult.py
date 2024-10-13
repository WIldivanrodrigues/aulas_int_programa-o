def tabuada ():
    from time import sleep

    print("*Tabuada de multiplicação*")
    numero = int(input("Insira o numero que você deseja ver a tabuada: "))

    for i in range(1, 11):
        resultado = numero * i
        sleep(1)
        print(f" {numero} x {i} = {resultado}")

tabuada()
