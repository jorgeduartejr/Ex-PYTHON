s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}.' .format(cont, s)) # terminar o ex para que a soma só aprensente o último valor