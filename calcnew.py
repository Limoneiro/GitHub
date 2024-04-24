opcao = 0
while (opcao != 9):
    print ( "--Escolha uma opção abaixo--")
    print ( "1. Adição")
    print ( "2. Subtração")
    print ( "3. Multiplicação")
    print ( "4. Divisão")
    print ( "5. Poteciação")
    opcao = int( input ( "Entre com uma opcao: "))
    if ( opcao == 5 ):
        print ( "--Escolha uma opção abaixo--")
        print ( "1. Quadrado")
        print ( "2. Cubo")
        print ( "3. Personalizado")
        opcao2 = int (input ("Entre com uma opção:"))
        n1 = float (input ("Entre com o Valor:"))
    elif ( opcao > 0 and opcao < 5 ):
        n1 = float (input ("Entre com o primeiro valor:"))
        n2 = float (input ("Entre com o segundo valor:"))
    resultado = 0
    if (opcao == 1):
        resultado = n1 + n2
    elif (opcao == 2):
        resultado = n1 - n2
    elif (opcao == 3):
        resultado = n1 * n2
    elif (opcao == 4):
        resultado = n1 / n2     #cálculo de potência
    elif (opcao == 5):                         #quadrado
        if ( opcao2 == 1 ):
            resultado = n1 * n1
        elif (opcao2 == 2 ):                   #cubo
            count = 2
            n2 = n1
            while ( count != 0 ):
                n1 = n1 * n2                   #dois valores, em que um se mantém inalterável para que funcione após o segundo ciclo
                count = count - 1
            resultado = n1
        elif ( opcao2 == 3):                   #variados
            count = float(input( "Elevado a quanto?"))
            count = count - 1                  #subtração de contagem para desconsiderar a elevação à 1, que ocasiona em erros
            n2 = n1
            while ( count != 0):
                n1 = n1 * n2
                count = count - 1
            resultado = n1    
    elif (opcao == 9):
        opcao = 9
    else:
        print ( "Opção inválida! tente novamente!")
    import os
    os.system('cls')
    print("O resultado é:", resultado)