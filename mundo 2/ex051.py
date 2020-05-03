print('=='*15)
print('This is a PA, chorastes ?')
print('=='*15)
ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(1, 11):
    print(ptermo, end=' ')
    ptermo += razao
print('Acabou')