print('Condição de existência de um triângulo')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triangulo e ', end='')
    if r1 == r2 == r3:
        print('o triângulo é equilátero.')
    elif r1 != r2 != r3 != r1:
        print('o triângulo é escaleno.')
    else:
        print('o triângulo é isósceles.')





'''else:
    print('Os segmentos acima NÃO PODEM formar triângulo')'''


