from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    menu = int(input('Digite os seguintes comandos para as operaçãoes: '))
    if menu == 1:
        soma = num1 + num2
        print('A soma dos números solicitados é: {}'.format(soma))
    elif menu == 2:
        multiplicar = num1 * num2
        print('O produto dos números solicitados é: {}'.format(multiplicar))
    elif menu == 3:
        if num1 > num2:
            print('O maior número é {}.'.format(num1))
        else:
            print('O maior número é {}.'.format(num2))
    elif menu == 4:
        print('Informe os números novamente!')
        new1 = int(input('Digite um novo número: '))
        new2 = int(input('Digite um novo número: '))
        print('[ 1 ] somar')
        print('[ 2 ] multiplicar')
        print('[ 3 ] maior')
        print('[ 4 ] novos números')
        print('[ 5 ] sair do programa')
        menu = int(input('Digite os seguintes comandos para as operaçãoes: '))
        if menu == 1:
            soma = new1 + new2
            print('A soma dos números solicitados é: {}'.format(soma))
        elif menu == 2:
            multiplicar = new1 * new2
            print('O produto dos números solicitados é: {}'.format(multiplicar))
        elif menu == 3:
            if new1 > new2:
                print('O maior número é {}.'.format(new1))
            else:
                print('O maior número é {}.'.format(new2))
    if menu == 5:
        print('A aplicação será encerrada...')
        sleep(2)
        pass





