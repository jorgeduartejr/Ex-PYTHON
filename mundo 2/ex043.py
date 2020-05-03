#fórmula imc = peso / (altura)**2
print('Calculadora de IMC')
massa = float(input('Digite aqui sua massa corporal em Kg: '))
altura = float(input('Digite aqui a sua altura: '))
imc = massa/(altura)**2
print('O seu IMC é {}.' .format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obsidade morbida')
else:
    pass