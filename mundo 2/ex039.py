from datetime import datetime
print('Serviço militar obrigatório')
'''sexo = input('Digite qual é o sexo: ')
if sexo = 'Masculino':
    print('Você não precisa se alistar.') # verificar alguma hora o erro.
else:
    pass '''
nasc = int(input('Digite aqui o seu ano de nascimento: '))
now = datetime.now()  #(now.year) me dá o ano atual
alist  = now.year - nasc  #(anoatual - ano de nascimento)
print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, alist, now.year))
if 17 < alist < 18:
    print('Você está próximo a se alistar')
elif alist >= 18 and alist < 23:
    print('Voce já está na idade do alistamento obrigatório.')
elif alist > 23:
    print('Você passou do tempo de alistamento, deverá pagar uma multa!')
else:
    pass


