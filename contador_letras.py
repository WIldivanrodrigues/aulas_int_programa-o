def contador_de_letras():
    frase = input("insira sua frase preferida: ").lower()

    vogais = "aeiou"
    vogais_contadas = 0 
    consoantes = 0

    for caractere in frase:
        if frase.isalpha():
            if caractere in vogais:
                vogais_contadas  +=1
            else:
                consoantes += 1

    print(f"Numero de vogais {vogais_contadas}.")
    print(f"consoantes contadas {consoantes}.")

contador_de_letras()
    
        
        
  

