from random import randint
computador = randint(0, 10) #faz o computador pensar em um número no intervalo
c = 0
while c != computador:
    jogador = int(input('Digite aqui o número: '))
    c += 1
    if jogador > computador:
        print('Escolha um número menor!')
    if jogador < computador:
        print('Escolha um número maior!')
    if jogador == computador:
        print('Você acertou!')
        print('Jogador escolheu {} e o computador {}!'.format(jogador, computador))
        print('Você fez {} jogadas até acertar!' .format(c))














