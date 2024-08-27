n1 = int(input('Digite um número inteiro: '))
n2 = 0
cont = 1
print(f'A tabuada do número {n1} é: ')
while cont < 12:
    print(f'{n1} x {n2} = ', n1*n2)
    n2 = n2 + 1
    cont = cont + 1
