from datetime import datetime
print('Confederação nacional de natacão')
nasc = int(input('Por favor, insira os seu ano de nascimento aqui: '))
anoatual = datetime.now() #(anoatual.year)
atleta = anoatual.year - nasc # ano atual - ano de nascimento
print('Voce possue {} anos, veja abaixo a sua categoria:' .format(atleta))
if atleta <= 9:
    print('Você é da categoria mirim.')
elif 9 < atleta <= 14:
    print('Você é da categoria infantil.')
elif 14 < atleta <= 19:
    print('Voce é da categoria Júnior.')
elif 19 < atleta <= 20:
    print('Você é da categoria Sênior.')
elif atleta > 20:
    print('Você é da categoria Master.')
else:
    pass




