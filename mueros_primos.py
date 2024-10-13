



#Regra 1 - precisa ser maior que 1

#Regra 2 - só pode ser divisível por 1 e ele mesmo

#Regra 3 - Dois é o único numero primo que é par.
if __name__ == "__main__":

    n = int(input("insira o número desejado: "))
    e_primo = True

    for i in range(n, 0, -1):

        if (n % i ) == 0:
            if n > 1 and i !=n and i != 1:
                e_primo = False

print(f"o número {n} é primo ? {e_primo}")
