#como fazer fatorial usando math lib
#from math import factorial
#fac = int(input('Digite aqui um número: '))
#print('O fatorial de {} é {}.'.format(fac, factorial(fac)))

#usando while
n = int(input('Digite aqui o número que quer o fatorial: '))
print('Calculando o {}! fatorial: '.format(n), end=' ')
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))