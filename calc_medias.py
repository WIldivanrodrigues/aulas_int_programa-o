print("Calculadora de médias de notas.")

def calcular_notas():
    notas = []
   
    while True:

        nota = float(input("insira a nota do aluno ( ou -1 para encerrar): "))
        if nota == -1:
            break
        elif 0<= nota <= 10:
            notas.append (nota)
        else:
            print("Por favor, insira uma nota válida em 0 e 10.")

    if notas:
        media = sum (notas) / len (notas)
        print(f"Sua média é {media:.2f}.")
        
        if media > 7.0 and  media <= 8.9:
            print(f"aprovado por média.")
        elif media < 7.0:
            print(f"você está na final.")
        elif media >= 9.0:
            print(f"aprovado com excelência.")
    
    else:
        print("nenhuma nota foi inserida.")

calcular_notas()

















#while True:
#    print("Calculadora de médias.")
#    print("insira 2 para inserir a sua nota: ")
#    print("Insira 3 para exibir a sua média: ")
#    print("insira 0 para sair: ")

#    nota = float(input("insira a sua nota: "))

