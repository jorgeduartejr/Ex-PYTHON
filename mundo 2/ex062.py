print('This is a PA V2, chorastes ?')
ptermo = int(input('Digite aqui o primeiro termo: '))
razão = int(input('Digite aqui a razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        c += 1
        print('{} ->'.format(ptermo), end =' ') #tem uma diferença entre colocar o ptermo antes e depois do print
        ptermo += razão         #colocando antes, a pa só começa do 2 termo
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer a mais ? '))
    print('Você solicitou {} termos.'.format(total))
    print('fim')

