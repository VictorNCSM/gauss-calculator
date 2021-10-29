def mmc(n, n2):

    minimo = False

    # Determina qual o menor e o maior número, pois o cálculo dos múltiplos ocorre em torno do menor número
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
    p = float(input("Insira o valor de p: "))
    plinha = float(input("Insira o valor de p': "))
    print("=========================================================================")

    if p == plinha:
        numerador = 2
        denominador = plinha

        # Invertendo os valores, já que após a regra de três numerador e denominador são trocados entre si
        f = denominador / numerador

        print(f"\nO valor de f é igual a: {f}")
    else:
        denominador = mmc(p, plinha)
        numerador = (denominador / plinha) + (denominador / p)
        f = denominador / numerador

        print(f"\nO valor de f é igual a: {f}")

elif var == "p" or var == "P":

    f = float(input("Insira o valor de f: "))
    plinha = float(input("Insira o valor de p': "))
    print("=========================================================================")

    if f == plinha:
        p = 0
        print(f"\nO valor de p é igual a: {p}")
    else:
        denominador = mmc(f, plinha)
        numerador = (denominador / f) - (denominador / plinha)
        p = denominador / numerador

        print(f"\nO valor de p é igual a: {p}")

elif var == "p'" or var == "P'":
    f = float(input("Insira o valor de f: "))
    p = float(input("Insira o valor de p: "))
    print("=========================================================================")

    if f == p:
        plinha = 0
        print(f"\nO valor de p' é igual a: {plinha}")
    else:
        denominador = mmc(f, p)
        numerador = (denominador / f) - (denominador / p)
        plinha = denominador / numerador
        print(f"\nO valor de p' é igual a: {plinha}")

else:
    var = input('O valor que você inseriu está incorreto. Digite "f", ou "p" ou "p\'"')
