from random import randint

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
        
        float(string)
        return True
    except:
        return False


string = ["\nVocê sabia?\n\nEspelho convexo\nAs suas vantagens: Ele amplia o campo de visão, por isso é usado por motoristas de ônibus; ele dá mais visão, porém a imagem é pequena.\n=============================================================================================\nEspelho côncavo:\nDeixa a imagem maior, e dependendo da distância podemos ver a imagem invertida.\n","\nVocê sabia? \n\nOs raios notáveis descritos são um artifício que facilita a determinação das características da imagem conjugada pelo espelho côncavo. Seu uso deve-se ao fato de que quaisquer raios de luz que incidam em superfícies refletoras côncavas serão refletidos assim como os raios notáveis o são.","\nVocê sabia?\n\nOs primeiros espelhos surgiram entre 5000 e 3000 A.C, não se sabe o lugar exato, alguns dizem ser na Suméria, porém as imagens do espelho não eram nítidas, porque era usado o bronze para produzi-las. Foi a partir do séc. 14, na Itália, que foram feitos os primeiros espelhos de vidro, após  ser realizada uma mistura de estanho e mercúrio. Todavia, muitas vezes os artesãos acabavam se contaminando, devido ao fato de que o mercúrio é um material extremamente poluente, e foi somente no século 19 que uma nova técnica foi desenvolvida, usando agora a prata química, ao invés do mercúrio."]


var = input("Digite a variável que você precisa saber: ")
valido = ["f", "F", "p", "P", "p'", "P'"]
passagem = var in valido

while not passagem:
    print("\nO que você digitou é inválido. As opções válidas são as seguintes: \n")
    print('Caso queira saber o valor de f, insira "f" ou "F" (sem aspas) para que possamos coletar;')
    print('Caso queira saber o valor de p, insira "p" ou "P" (sem aspas) para que possamos coletar;')
    print('E por fim, caso queira saber o valor de p\', insira "p\'" ou "P\'" (sem aspas) para que possamos coletar.')
    print("=============================================================================================\n")
    var = input("Digite a variável que você precisa saber: ")
    passagem = var in valido


if var == "f" or var == "F":
    p = input("Insira o valor de p: ")
    plinha = input("Insira o valor de p': ")
    print("=============================================================================================")

    while valid(p) == False or valid(plinha) == False:
        print("Os valores que você inseriu estão incorretos. Por gentileza, insira valores numéricos.")
        p = input("Digite o valor de p: ")
        plinha = input("Digite o valor de p': ")
        print("=============================================================================================")
    else:
        p = float(p)
        plinha = float(plinha)
        
   

    if p == 0 or plinha == 0:

        if p == 0 and plinha == 0:
            f = plinha
        elif p == 0:
            f = 0
        else:
            f = p

        print(f"O valor de f é igual a: {f:.2f}")
        print("==============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")
        
        
    elif p == plinha:
        numerador = 2
        denominador = plinha

        # Invertendo os valores, já que após a regra de três numerador e denominador são trocados entre si
        f = denominador / numerador

        print(f"O valor de f é igual a: {f:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")
        
    else:
        denominador = mmc(p, plinha)
        numerador = (denominador / plinha) + (denominador / p)
        f = denominador / numerador

        print(f"O valor de f é igual a: {f:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")

elif var == "p" or var == "P":

    f = input("Insira o valor de f: ")
    plinha = input("Insira o valor de p': ")
    print("=============================================================================================")

    while valid(f) == False or valid(plinha) == False:
        print("Os valores que você inseriu estão incorretos. Por gentileza, insira valores numéricos.")
        f = input("Digite o valor de f: ")
        plinha = input("Digite o valor de p': ")
        print("=============================================================================================")
    else:
        f = float(f)
        plinha = float(plinha)



    if f == 0 or plinha == 0:


        if f == 0 and plinha == 0:
            p = 0
        elif f == 0:
            p = plinha - (plinha * 2)
        else:
            p = f

        print(f"O valor de p é igual a: {p:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")
        
    elif f == plinha:

        p = 0
        print(f"O valor de p é igual a: {p:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")

    else:
        denominador = mmc(f, plinha)
        numerador = (denominador / f) - (denominador / plinha)
        p = denominador / numerador

        print(f"O valor de p é igual a: {p:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")

elif var == "p'" or var == "P'":
    f = input("Insira o valor de f: ")
    p = input("Insira o valor de p: ")
    print("==============================================================================================\n")

    while valid(f) == False or valid(p) == False:
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
            
        print(f"O valor de p' é igual a: {plinha:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")

    elif f == p:
        plinha = 0
        print(f"O valor de p' é igual a: {plinha:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")
        
    else:
        denominador = mmc(f, p)
        numerador = (denominador / f) - (denominador / p)
        plinha = denominador / numerador
        
        print(f"O valor de p' é igual a: {plinha:.2f}")
        print("=============================================================================================\n")
        print("\n", string[randint(0, 2)])
        input("Pressione enter para sair.")

else:
    pass
