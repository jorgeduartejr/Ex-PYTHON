print('Condição de existência de um número primo')
tot = 0
num = int(input('Digite aqui um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 O número {}, foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('Ele NÃO É PRIMO.')
