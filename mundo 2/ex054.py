from datetime import datetime
data = datetime.now()
anoatual = data.year #variável que indica a o ano atual
totalmaior = 0
totalmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pess)))
    idade = anoatual - nasc
    if idade >= 18:
        totalmaior += 1
    else:
       totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade.' .format(totalmaior, totalmenor))
