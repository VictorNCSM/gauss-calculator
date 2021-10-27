def mmc(n,n2)
    n = int(input("primeiro número do MMC: "))
    n2 = int(input("Segundo número do mmc"))

    if n > n2:
        num = n
    else:
        num = n2
        
        
    cont = 0

    while n != 1 and n2 != 1:
        
        # For para pegar todos os números do intervalo
        for i in range(1,num + 1):
            
            # For para testar cada número do intervalo
            for a in range(1,i + 1):
                
                if a % 2 == 0:
                    cont += 1

            # Se o número for primo, realizaremos as divisões
            if cont == 2:
                
                # Se os dois forem divisíveis por i
                if n % i and n2 % 1 == 0:
                    n = n / i
                    n2 = n2 / i
                    cont = 0 
                    
                # Se só o n for divisível
                elif n % i == 0 and n2 % i != 0:
                    n = n / i
                    cont = 0
                
                # Se só o n2 for divisível
                elif n2 % 1 == 0 and n1 % 1 != 0:
                    n2 = n2 / i
                    cont = 0
                else:
                    cont = 0
                    pass
            else:
                cont = 0        

var = input("Digite a variável que você precisa saber: ")

if var == "f" or var == "F":
    p = float(input("Insira o valor de p: "))
    plinha = float(input("Insira o valor de p': "))
    
    if p == plinha:
        numerador = 1 + 1
        denominador = plinha
        fracao = [numerador,denominador]
        
    else:
        
            
                   
elif var == "p" or var == "P":
    
    f = float(input("Insira o valor de f: "))
    plinha = float(input("Insira o valor de p': "))
         
elif var == "p'" or var == "P'":
    a = 4
else: 
    var = input('O valor que você inseriu está incorreto. Digite "f", ou "p" ou "p\'"')