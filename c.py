num = int(input("Digite o número: "))

cont = 0
# For para pegar todos os números do intervalo
for i in range(1, num + 1):
    print(f"\n O número a ser testado agora será o {i} \n")

    # For para testar cada número do intervalo
    for a in range(1, i + 1):

        if i % a == 0:
            print(f"A divisão a ser realizada é {i} / {a}")
            cont += 1
            print(cont)

    # Se o número for primo, realizaremos as divisões
    if cont == 2:
        print(f"O número realizou somente {cont} divisões, portanto, {i} é primo.")
        cont = 0
    else:
        print(f"O número não é primo, pois realizou {cont} divisões \n ============================================")
        cont = 0
