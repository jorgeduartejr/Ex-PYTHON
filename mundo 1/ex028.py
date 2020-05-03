from random import randint
from time import sleep
computador = randint(0,5) #faz o computador escolher um numero
print('Você consegue advinhar o número que eu pensei ?')
jogador = int(input('Digite um número entre 0 e 5: ')) #jogador escolhe um numero
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você venceu!!')
else:
    print('Eu pensei no número {} e não no {} logo você perdeu, tente novamente' .format(computador, jogador))
