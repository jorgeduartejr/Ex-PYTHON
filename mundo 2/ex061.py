print('This is a PA V2, chorastes ?')
ptermo = int(input('Digite aqui o primeiro termo: '))
razão = int(input('Digite aqui a razão: '))
c = 0
while c < 11:
    c += 1
    print(ptermo, end =' ') #tem uma diferença entre colocar o ptermo antes e depois do print
    ptermo += razão         #colocando antes, a pa só começa do 2 termo
print('FIM')

