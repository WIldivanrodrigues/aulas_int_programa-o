#calculando sequencia de fibonate
#desenvolva um programa que gere os primeiros n números 
# da sequencia de fibonacci.


if __name__=='__main__':

#Onde n é fornecido pelo usuário
    n = int(input("digite o número desejado: "))
    range(10)
    fn1 = 0
    fn2 = 1

#utilize um loop para calcular e exibir os termos da sequência

    for i in range(n):
        resultado = fn1 + fn2
        fn1 = fn2
        fn2 = resultado
        print(f"resultado {resultado} | fn1 => {fn1} | fn2 = > {fn2} .  ")