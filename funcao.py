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