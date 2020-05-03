from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
# print('O computador escolheu {}' .format(itens[computador]))
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 11)
print('Computador jogou {}' .format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('O JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

else:
    pass












'''import random
lista = (['Pedra', 'Papel', 'Tesoura'])
escolhapc = random.choice(lista)
# print(random.choice(lista)
a = 'Pedra'
b = 'Papel'
c = 'Tesoura'
print('Jokempo!')
print('Escolha entre pedra, papel ou tesoura')
escolha = input('Digite aqui a sua escolha: ')
print('O computador escolheu {}' .format(escolhapc))
if escolha == escolhapc:
    print('Deu empate, escolha novamente!')
elif a > c :
    print('Pedra ganhou!')
elif c > b:
    print('Tesoura ganhou!')
elif b > a :
    print('Papel ganha de pedra!')'''

