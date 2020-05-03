vel = int(input('Qual é a velocidade que você estava ? '))
if vel > 80:
    print('Você foi multado, reduza a velocidade')
    multa = (vel - 80) * 7
    print('Você pagará uma multa de {} reais.' .format(multa))
else:
    print('Você está indo bem, continue assim.')