nome1 =str(input("nome jogador 1: "))
nome2 =str(input("nome jogador 2: "))

jogador1 = 0
jogador2 = 0
rodada = 0

while  (jogador1 > 0 or jogador2 < 2) and (jogador1 < 2 or jogador2 > 0) and (rodada < 3):

    rodada += 1

    print("1- pedra, 2- papel, 3- tesoura")
    jogada1 = int(input("opção jogador 1: "))


    print("1- pedra, 2- papel, 3- tesoura")
    jogada2 = int(input("opção jogador 2: "))

    if jogada1 == 1 and jogada2 == 2 :
        print(nome2)
        jogador2 +=1
        pass

    if jogada1 == 2 and jogada2 == 3 :
        print(nome2)
        jogador2 +=1
        pass

    if jogada1 == 1 and jogada2 == 3 :
        print(nome1)
        jogador1 +=1
        pass

    if jogada1 == 3 and jogada2 == 1 :
        print(nome2)
        jogador2 +=1
        pass

    if jogada2 == 1 and jogada1 == 2 :
        print(nome1)
        jogador1 +=1
        pass

    if jogada2 == 2 and jogada1 == 3 :
        print(nome1)
        jogador1 +=1
        pass

    if jogada1 == jogada2 :
        print("igual")
        pass

    print("pontos jogador 1: ", jogador1)
    print("pontos jogador 2: ", jogador2)

if jogador1 > jogador2 :
    vencedor = nome1
    print("vencedor: ",vencedor,"pontos: ", jogador1)
else :
    vencedor = nome2
    print("vencedor: ",vencedor,"pontos: ", jogador2)