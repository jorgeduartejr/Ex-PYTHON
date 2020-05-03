nota1 = float(input('Digite aqui a sua primera nota: '))
nota2 = float(input('Digite aqui a sua segunda nota: '))
media = (nota1+nota2)/2

if media < 5:
    print('Você está reprovado')
elif media >= 5 and media <= 6.9:
    print('Você está de recuperação')
elif media >= 7:
    print('Voce está aprovado')
else:
    pass






