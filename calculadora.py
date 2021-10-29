def mmc(n, n2):

    minimo = False

    # Determina qual o menor e o maior número, pois o cálculo dos múltiplos ocorre em torno no menor número
    if n < n2:
        menor = n
        maior = n2
    else:
        menor = n2
        maior = n

    i = 1 # Inicialização da variável de contagem

    # Enquanto o mínimo não tiver sido encontrado, ele continuará procurando
    while not minimo:
        a = menor * i

        # O primeiro múltiplo do menor que compuser uma divisão exata com o maior será o MMC
        if a % maior == 0:
            minimo = a

        i += 1

    return minimo


var = input("Digite a variável que você precisa saber: ")

if var == "f" or var == "F":
    p = float(input("Insira o valor de p: "))
    plinha = float(input("Insira o valor de p': "))

    if p == plinha:
        numerador = 1 + 1
        denominador = plinha
        # Invertendo os valores, já que após a regra de três numerador e denominador são trocados entre si
        fracao = {'numerador': denominador, 'denominador': numerador}
    else:
        denominador = mmc(p, plinha)
        numerador = (denominador / plinha) + (denominador / p)
        f = denominador / numerador


elif var == "p" or var == "P":
    
    f = float(input("Insira o valor de f: "))
    plinha = float(input("Insira o valor de p': "))
         
elif var == "p'" or var == "P'":
    a = 4
else: 
    var = input('O valor que você inseriu está incorreto. Digite "f", ou "p" ou "p\'"')
