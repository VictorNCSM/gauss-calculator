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
