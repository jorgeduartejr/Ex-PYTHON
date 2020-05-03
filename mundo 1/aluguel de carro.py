kmrodado = int(input("Digite quantos km foram rodados: "))
diasrodados = int(input("Digite quantos dias foram rodados: "))
total = kmrodado + diasrodados
valorkm = kmrodado * 0.15
valordias = diasrodados * 60
totalapagar = valorkm + valordias

print('O valor total para pagamento é de R${:.2F}'.format(totalapagar))
