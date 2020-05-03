import math
x = int(input('Digite aqui o ângulo desejado: '))
A = math.sin(x)
B = math.cos(x)
C = math.tan(x)

print('O valor do seno é {:.2f}, do cosseno {:.2f} e da tangente {:.2F}'.format(A, B, C))
