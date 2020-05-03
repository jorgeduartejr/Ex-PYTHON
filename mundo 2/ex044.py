print('Calculadora de preços')
print('--' * 10)
valor = float(input('Digite o valor do produto: '))
print('''Escolha uma forma de pagamento:
[1] à vista no dinheiro/cheque com 10% de desconto.
[2] à vista no cartão com 5% de desconto.
[3] em até 2x no cartão (preço normal sem desconto).
[4] 3x ou mais no cartao com acréscimo de 20% de juros. ''')
opção = int(input('Digite aqui a sua opção: '))
if opção == 1:
    print('O valor será de {}.' .format(valor - (valor*0.1)))
elif opção == 2:
    print('O valor a ser pago será {}.' .format(valor-(valor*0.05)))
elif opção == 3:
    print('O valor será de {}.' .format(valor))
elif opção == 4:
    print('O valor será de {}.' .format(valor + (valor*0.2)))
else:
    print('Insira um valor válido')



