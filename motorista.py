from datetime import date
import os

data = date.today()
data = '{}/{}/{}'.format(data.day, data.month, data.year)

nome = input ( "Insira seu nome: " )
cod = int ( input ( "Insira seu número de identificação: ") )
os.system('cls')

placa = input ( "Insira a placa do veículo: " )
nv = int ( input ( "Insira o número do veículo: " ) )
os.system('cls')

kmi = int ( input ( "Insira a quilometragem inicial: " ) )
kmf = int ( input ( "Insira a quilometragem final: ") )
kmt = kmf - kmi
os.system('cls')

tipoc = 0
while ( tipoc <= 0 or tipoc > 4 ):
    print ( "Insira o tipo de combustível utilizado:" )
    print ( "1. Diesel" )
    print ( "2. Gasolina" )
    print ( "3. Etanol" )
    print ( "4. Álcool")
    tipoc = int ( input ( " " ) )
os.system('cls')

litros = int ( input ( "Insira quantos litros foram utilizados: ") )
media = kmt / litros
os.system ('cls')

print ( data )
print ( "----------------------------------------------------" )
print ( "                    MOTORISTA                       " )
print ( "----------------------------------------------------" )
print ( "N° de Identificação: " , cod )
print ( " " )
print ( "Motorista: " , nome )
print ( " " )
print ( "----------------------------------------------------" )
print ( "                     VEÍCULO                        " )
print ( "----------------------------------------------------" )
print ( "Placa: " , placa )
print ( " " )
print ( "N° do Veículo: " , nv )
print ( " " )
print ( "KM Inicial: " , kmi )
print ( "KM Final: " , kmf )
print ( " " )
print ( "Total KM: " , kmt )
print ( " " )
print ( "----------------------------------------------------" )
print ( "                  ABASTECIMENTO                     " )
print ( "----------------------------------------------------" )

if ( tipoc == 1 ):
    preco = 5.85
    print ( "Tipo: Diesel" )
    print ( " " )
    print ( "Preço/Litro: R$" , preco )
elif ( tipoc == 2 ):
    preco = 5.78
    print ( "Tipo: Gasolina" )
    print ( " " )
    print ( "Preço/Litro: R$" , preco )
elif ( tipoc == 3 ):
    preco = 3.53
    print ( "Tipo: Etanol" )
    print ( " " )
    print ( "Preço/Litro: R$" , preco )
elif ( tipoc == 4 ):
    preco = 3.42
    print ( "Tipo: Álcool" )
    print ( " " )
    print ( "Preço/Litro: R$", preco )
precol = preco * litros

print ( " " )
print ( "Litros: " , litros)
print ( "Gasto total: " , precol )
print ( "----------------------------------------------------" )
print ( "                      MÉDIA                         " )
print ( "----------------------------------------------------" )
print ( "Média: ", media , "Km/l" )
print ( " " )
print ( "----------------------------------------------------" )
print ( "                    RESULTADO                       " )
print ( "----------------------------------------------------" )

if ( media < 9 ):
    print ( "Status: Abaixo da Média" )
elif ( media >= 9 and media <= 10 ):
    print ( "Status: Dentro da Média" )
elif ( media > 10 ):
    print ( "Status: Acima da Média" )
print ( " " )
print ( "----------------------------------------------------" )
print ( "----------------------------------------------------" )