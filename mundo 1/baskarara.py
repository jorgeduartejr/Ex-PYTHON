import math

a = int(input("Qual o valor da variável a?"))
b = int(input("Qual o valor da variável b?"))
c = int(input("Qual o valor da variável c?"))

Delta = ( b** 2 - 4 * a * c)
X = ( - b + math.sqrt(Delta))/ (2 * a)
X = ( - b - math.sqrt(Delta))/ (2 * a)


