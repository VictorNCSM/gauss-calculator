def mmc(n, n2):
    if n < n2:
        menor = n
        maior = n2
    else:
        menor = n2
        maior = n

    i = 1
    minimo = False

    while not minimo:
        a = menor * i


        if a % maior == 0:
            minimo = a

        i += 1

    return minimo

def valid(string):
    try:
        if string == '0':
            return True
        return True
    except:
        return False


var = input("Digite a variável que você precisa saber: ")
valido = ["f", "F", "p", "P", "p'", "P'"]
passagem = var in valido

while not passagem:
    print("\nO que você digitou é inválido. As opções válidas são as seguintes: \n")
    print('Caso queira saber o valor de f, insira "f" ou "F" (sem aspas) para que possamos coletar;')
    print('Caso queira saber o valor de p, insira "p" ou "P" (sem aspas) para que possamos coletar;')
    print('E por fim, caso queira saber o valor de p\', insira "p\'" ou "P\'" (sem aspas) para que possamos coletar.')
    print("===================================================================================================================== \n")
    var = input("Digite a variável que você precisa saber: ")
    passagem = var in valido


if var == "f" or var == "F":
    p = input("Insira o valor de p: ")
    plinha = input("Insira o valor de p': ")
    print("=========================================================================")

    while not valid(p) or valid(plinha):
        print("Os valores que você inseriu estão incorretos. Por gentileza, insira valores numéricos.")
        p = input("Digite o valor de p: ")
        plinha = input("Digite o valor de p': ")
    else:
        p = float(p)
        plinha = float(plinha)


    if p == plinha:
        numerador = 2
        denominador = plinha

        # Invertendo os valores, já que após a regra de três numerador e denominador são trocados entre si
        f = denominador / numerador

        print(f"\nO valor de f é igual a: {f}")

    elif p == 0 or plinha == 0:

        if p == 0 and plinha == 0:
            f = plinha
        elif p == 0:
            f = 0
        else:
            f = p

        print(f"\nO valor de f é igual a: {f}")
    else:
        denominador = mmc(p, plinha)
        numerador = (denominador / plinha) + (denominador / p)
        f = denominador / numerador

        print(f"\nO valor de f é igual a: {f}")

elif var == "p" or var == "P":

    f = input("Insira o valor de f: ")
    plinha = input("Insira o valor de p': ")
    print("=========================================================================")

    while not valid(f) or valid(plinha):
        print("Os valores que você inseriu estão incorretos. Por gentileza, insira valores numéricos.")
        f = input("Digite o valor de f: ")
        plinha = input("Digite o valor de p': ")
    else:
        f = float(f)
        plinha = float(plinha)



    if f == 0 or plinha == 0:


        if f == 0 and plinha == 0:
            p == 0
        elif f == 0:
            p = plinha - (plinha * 2)
        else:
            p = f

        print(f"\nO valor de p é igual a: {p}")
    elif f == plinha:

        p = 0
        print(f"\nO valor de p é igual a: {p}")

    else:
        denominador = mmc(f, plinha)
        numerador = (denominador / f) - (denominador / plinha)
        p = denominador / numerador

        print(f"\nO valor de p é igual a: {p}")

elif var == "p'" or var == "P'":
    f = input("Insira o valor de f: ")
    p = input("Insira o valor de p: ")
    print("=========================================================================")

    while not valid(f) or valid(p):
        print("Os valores que você inseriu estão incorretos. Por gentileza, insira valores numéricos.")
        f = input("Digite o valor de f: ")
        p = input("Digite o valor de p: ")
    else:
        f = float(f)
        p = float(p)


    if p == 0 or f == 0:
        if p == 0 and f == 0:
            plinha = 0
        elif p == 0:
            plinha = f
        else:
            plinha = p - (p * 2)

    elif f == p:
        plinha = 0
        print(f"\nO valor de p' é igual a: {plinha}")
    else:
        denominador = mmc(f, p)
        numerador = (denominador / f) - (denominador / p)
        plinha = denominador / numerador
        print(f"\nO valor de p' é igual a: {plinha}")

else:
    var = input('O valor que você inseriu está incorreto. Digite "f", ou "p" ou "p\'"')
