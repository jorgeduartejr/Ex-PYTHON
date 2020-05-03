import math
catop = int(input('Digite aqui o valor do cateto oposto: '))
catad = int(input('Digite aqui o valor do cateto adjascente: '))
hip = math.sqrt(catop**2 + catad**2)
print('O valor do da hipotenusa é: ', hip)
