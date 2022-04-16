from time import sleep
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
op = 0
while op != 5:
    print('-=' * 15)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    op = int(input('>>>>Qual sua opção ?:  '))
    if op == 1:
        soma = n1 + n2
        print('A soma de {} com {} é igual a {}'.format(n1,n2,soma))
    elif op == 2:
        mult = n1 * n2
        print('O produto de {} com {} é igual a {}'.format(n1,n2,mult))
    elif op == 3:
        if n1 > n2:
            print('O maior é {} e o menor é {}'.format(n1,n2))
        else:
            print('O maior é {} e o menor é {}'.format(n2,n1))
    elif op == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif op == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Porfavor digite os numeros corretamente')

print('Obrigado por usar :)')
