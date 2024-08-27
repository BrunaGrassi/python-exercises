n1 = int(input(' Digite um número: '))
n2 = int(input(' Digite outro número: '))
soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1 * n2
elevado = n1 ** n2
divisaoInteira = n1 // n2
restoDivisao = n1 % n2

print(f' O resultado da soma é {soma}; \n O resultado da subtração é {subtracao}; \n O resultado da divisão é {divisao}; \n O resultado da multiplicação é {multiplicacao};', end=' ')
print(f'\n O resultado da exponenciação é {elevado}; \n O resultado da divisão inteira é {divisaoInteira}; \n E o resto da divisão é {restoDivisao};')