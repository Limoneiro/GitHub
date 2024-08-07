import random

vidamax = 10
vida = 10
manamax = 10
mana = 10
armadura = 0
gold = 10
arma = 1
pocaoc = 1
pocaom = 1
custoc = 2
custofb = 5
fases = [ "fase1" , "boss1" ,  "fase2" , "boss2", "fase3" , "boss3" ]

while ( vida > 0 ):
    tipo = 0
    for tipo in range (1 , 4 , 1):
        if ( arma == 1 ):
            ataque = 2
        elif ( arma == 2 ):
            ataque = 3
        elif ( arma == 3 ):
            ataque = 5
        inimigo = random.randint ( 1 , 3 )
        inimigo = 3
        if ( inimigo == 1 ):
            if (vida > 0 ):
                vidai = 10
                ataquei = 1
                premio = 3
                print ( "Um Chupaku apareceu!!")
                print (f'                 \n'
                        f'     |\     ____ \n'
                        f"     | \.-./ .-' \n"
                        f'     \ _  _(     \n'
                        f'     | .)(./     \n'
                        f'     |   \(      \n'
                        f'     |     \     \n'
                        f"     |   vvv     \n"
                        f'     |  |__      \n'
                        f'     /      `-.  \n')
        elif ( inimigo == 2 ):
            if (vida > 0 ):
                vidai = 15
                ataquei = 3
                premio = 5
                print ( "Um Mini Grifo apareceu!!")
                print (f'   ____       ____    \n'
                        f'  /    )     (    \   \n'
                        f' /    (  ^_^  )    \  \n'
                        f'|  (   \(°v°)/   )  | \n'
                        f'|   (   /   \   )   | \n'
                        f'| )(   /\   /\   )( | \n'
                        f'|)  (_ | \|/  |_)  (| \n'
                        f'      "--^^^^--"      \n')
        elif ( inimigo == 3 ):
            if (vida > 0 ):
                vidai = 20
                ataquei = 5
                premio = 10
                print ("Um Centauro apareceu!!")
                print ( f'         |)       \n'
                        f'     --.  /|      \n'
                        f"   _|''|../       \n"
                        f" .'| |  -'        \n"
                        f' :/ \()/          \n'
                        f"(L  /--',----._   \n"
                        f'    |          |\ \n'
                        f"   : /-\ .'-'\ / |\n"
                        f'    ||, ||    \|  \n'
                        f'     \/ ||    ||  \n')
        while ( vidai > 0 and vida > 0 ):
            if ( vida > 0 ):
                print ( "Vida do inimigo: ", vidai)
                print ( "Sua Vida: " , vida)
                print ( "Sua Mana: " , mana)
                print ( "1.Ataque 2.Magia 3.Item" )
                opcao = int ( input ( "" ))
                if ( opcao == 1 ):
                    chance = random.randint ( 1 , 100 )
                    if (chance > 0 and chance < 70):
                        vidai = vidai - ataque
                    elif (chance > 70 and chance < 90 ):
                        print ( "Você errou o ataque")
                    elif (chance > 90 ):
                        vidai = vidai - (ataque * 2)
                        print ("ataque crítico")
                elif ( opcao == 2 ):
                    print ( "1.Cura 2.Bola de fogo" )
                    magia = int ( input ( "" ))
                    if ( magia == 1):
                        if ( mana >= custoc ):
                            if ( vida == vidamax ):
                                vida = vidamax
                            elif ( vida < vidamax):
                                vida = vida + 5
                                if ( vida > vidamax):
                                    vida = vidamax
                            mana = mana - custoc
                    elif ( magia == 2 ):
                        if ( mana >= custofb ):
                            vidai = vidai - 5
                            mana = mana - custofb
                elif ( opcao == 3 ):
                    print ( "Poçôes de cura : " , pocaoc)
                    print ( "Poçôes de mana : " , pocaom)
                    print ( "1.Poção de cura 2.Poção de Mana" )
                    item = int ( input( "" ))
                    if ( item == 1 ):
                        if (pocaoc >= 1 ):
                            if ( vida == vidamax ):
                                vida = vidamax
                            elif ( vida < vidamax):
                                vida = vida + 5
                                if ( vida > vidamax):
                                    vida = vidamax
                            pocaoc = pocaoc - 1
                    elif ( item == 2 ):
                        if (pocaom >= 1 ):
                            if ( mana == manamax ):
                                mana = manamax
                            elif ( mana < manamax):
                                mana = mana + 5
                                if ( mana > manamax):
                                    mana = manamax
                        pocaom = pocaom - 1
                print ( "O inimigo te ataca!")
                if ((ataquei - armadura) <= 0 ):
                    vida = vida
                    print ( "Ele te causou 0 de dano")
                else:
                    vida = vida - ( ataquei - armadura )
                    print ( f'Ele te causou {ataquei - armadura} de dano')
                if ( vida < 0 ):
                    vida = 0
                if ( vidai < 0 ):
                    vidai = 0
        if ( vidai < 0):
            gold = gold + premio
            print ("Você ganhou " , premio , " de gold!!!")
            print ( "Agora você tem " , gold , " de gold")
    if ( vida > 0 ):
        custoem = 10
        custoeb = 20
        custopc = 10
        custopm = 10
        custoam = 15
        custoap = 25
        customv = 30
        customm = 30
        custocp = 25
        print ( "LOJA")
        print ( "Bem vindo a loja!!")
        print ( "deseja comprar algo?")
        print ( "ARMAS:")
        print ( "1.Espada Média : " , custoem , "de gold" )
        print ( "2.Espada Boa : " , custoeb , "de gold" )
        print ( "POÇÔES:")
        print ( "3.Poção de cura : " , custopc , "de gold" )
        print ( "4.Poção de mana :" , custopm , "de gold" )
        print ( "ARMADURA:")
        print ( "5.Armadura leve :" , custoam , "de gold" )
        print ( "6.armadura pesada :" , custoap , "de gold" )
        print ( "MELHORIAS:")
        print ( "7.Aumento de vida" , customv , "de gold" )
        print ( "8.Aumento de mana" , customm , "de gold" )
        print ( "CURA:")
        print ( "9.Cura completa" , custocp )
        print ( "Digite 9 para sair")
        produto = int (input( "" ))
        if ( produto == 1 ):
            if ( gold >= custoem ):
                arma = 2
                gold = gold - custoem
            else:
                print ( "Você não tem gold o suficiente" )
        elif ( produto == 2 ):
            if ( gold >= custoeb ):
                arma = 3
                gold = gold - custoeb
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 3 ):
            if ( gold >= custopc ):
                pocaoc = pocaoc + 1
                gold = gold - custopc
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 4 ):
            if ( gold >= custopm ):
                pocaom = pocaom + 1
                gold = gold - custopm
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 5 ):
            if ( gold >= custoam ):
                armadura = 2
                gold = gold - custoam
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 6 ):
            if ( gold >= custoap ):
                armadura = 4
                gold = gold - custoap
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 7 ):
            if ( gold >= customv ):
                vidamax = vidamax + 2
                gold = gold - customv
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 8 ):
            if ( gold >= customm ):
                vidamax = vidamax + 2
                gold = gold - customm
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
        elif ( produto == 9 ):
            if ( gold >= custocp ):
                vida = vidamax
                mana = manamax
                gold = gold - custocp
                print ( "Bela compra!! agora você tem " , gold , "de gold")
            else:
                print ( "Você não tem gold o suficiente")
print ( f'\n'
        f'\n'
        f'VOCÊ MORREU!!\n'
        f" .-. \n"
        f"(OvO) \n"
        f" |=| \n")
#Faça listas e fases de inimigos