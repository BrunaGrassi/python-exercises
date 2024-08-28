# calcula a raiz quadrada de um número informado
# metodo de importação diferente do ex015

from math import sqrt
num = int(input('Informe um número: '))
raiz = sqrt(num)

print('A raiz quadrada do número {} é {:.2f}'.format(num, raiz))